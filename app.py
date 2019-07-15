# EXAMPLE OF A WORKING FLASK APPLICATION

# import flask functionality in order to set up the application for use
import os
from flask import Flask

app = Flask(__name__)

# remember the "/" refers to the default route 
@app.route("/")
def hello():
  return "Hello World ...again"

if __name__ == "__main__":
  # app.run() function we set the host, we use the os import, we use the getenv object and then we get the IP
  # The following code works for production (heroku)
  app.run(host=os.getenv("IP", "0.0.0.0"),
  # then we set the port, and we convert the port to an integer
  # The following code works for production (heroku)
  port=int(os.getenv("Port", "8080")), debug=True)
  # last parameter we want to pass is debug. By setting it to true, it allows the changes to be picked up automatically in the browser.
  # below syntax is for opening project locally not production (heroku)
  # app.run(debug=True)