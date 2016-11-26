from flask import Flask, request

app = Flask(__name__)

@app.route("/example/rule/<name>", methods=["GET", "POST"])
def example_environ(name):
    print(request.view_args)
    return ""

app.run()