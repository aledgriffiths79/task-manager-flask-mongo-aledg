# EXAMPLE OF A WORKING FLASK APPLICATION

# import flask functionality in order to set up the application for use
import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = "task_manager"
app.config["MONGO_URI"] = "mongodb+srv://aledgriffiths79:motoisfun38@myfirstcluster-wlh95.mongodb.net/task_manager?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_tasks")

# remember the "/" refers to the default route 
def get_tasks():
  return render_template("tasks.html", tasks=mongo.db.tasks.find())

@app.route("/add_task")
def add_task():
  return render_template("addtask.html", categories=mongo.db.categories.find())

@app.route("/insert_task", methods=["POST"]) #testing /insert_task
def insert_task():
  tasks = mongo.db.tasks
  tasks.insert_one(request.form.to_dict())
  return redirect(url_for("get_tasks"))

@app.route("/edit_task/<task_id>")
def edit_task(task_id):
  the_task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
  all_categories = mongo.db.categories.find()
  return render_template("edittask.html", task=the_task, categories=all_categories)

@app.route("/update_task/<task_id>", methods=["POST"])
def update_task(task_id):
  tasks = mongo.db.tasks
  tasks.update( {"_id": ObjectId(task_id)},
  {
    'task_name': request.form.get('task_name'),
    'category_name': request.form.get('category_name'),
    'task_description': request.form.get('task_description'),
    'due_date': request.form.get('due_date'),
    'is_urgent': request.form.get('is_urgent')
  })
  return redirect(url_for('get_tasks'))

@app.route("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    return redirect(url_for("get_tasks"))



if __name__ == '__main__':
    # app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True) 
  # app.run() function we set the host, we use the os import, we use the getenv object and then we get the IP
  # The following code works for production (heroku)
  # app.run(host=os.getenv("IP"),
  # then we set the port, and we convert the port to an integer
  # The following code works for production (heroku)
  # port=int(os.getenv("PORT")))
  # last parameter we want to pass is debug. By setting it to true, it allows the changes to be picked up automatically in the browser.
  # below syntax is for opening project locally not production (heroku)
  app.run(debug=True)

  # When i run app.py in cmd terminal with app.run syntax in production it will output "TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'"     Why? Because your IP and PORT are set by default on your local machine, which is why you need just app.run() , but with Heroku, you have to specify. 