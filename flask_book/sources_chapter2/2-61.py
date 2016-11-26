from flask import Flask, request

app = Flask(__name__)

@app.route("/example/max_content_len", methods=["GET"])
def example_content_length():
    print(request.max_content_length)
    return ""

app.run()