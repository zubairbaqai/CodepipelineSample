from flask import Flask
import time

application = Flask(__name__)

@application.route("/")
def index():
    return "Your Flask App Works!"

@application.route("/hello")
def hello():
    time.sleep(60)
    return "Hello World!"


if __name__ == "__main__":
    application.run(port=5000, debug=True)