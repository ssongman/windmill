from flask import Flask, request

app = Flask(__name__)

@app.route("/example/json", methods=["POST"])
def example_json():
    print(request.get_json())
    return ""

app.run()