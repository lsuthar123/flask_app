from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_view():
    return "<h1>Hello, as per your requirement flask app is deployed 😊</h1>"
