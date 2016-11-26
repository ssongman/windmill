from flask import Flask, request

app = Flask(__name__)

@app.route("/example/environ", methods=["GET", "POST"])
def example_environ():
    return request.method

app.run()