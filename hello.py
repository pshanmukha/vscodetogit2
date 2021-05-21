from flask import Flask
myapp = Flask(__name__)

@myapp.route("/")
def hello():
    return "Just connected from VScode to Github with added word another change and"