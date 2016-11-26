from flask import Flask, request

app = Flask(__name__)

@app.route("/example/rule", methods=["GET", "POST"])
def example_rule():
    return request.url_rule

app.run()