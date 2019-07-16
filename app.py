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


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True) 
# if __name__ == "__main__":
  # app.run() function we set the host, we use the os import, we use the getenv object and then we get the IP
  # The following code works for production (heroku)
  # app.run(host=os.getenv("IP"),
  # then we set the port, and we convert the port to an integer
  # The following code works for production (heroku)
  # port=int(os.getenv("PORT")))
  # last parameter we want to pass is debug. By setting it to true, it allows the changes to be picked up automatically in the browser.
  # below syntax is for opening project locally not production (heroku)
  # app.run(debug=True)

  