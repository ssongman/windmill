from flask import request

@app.route("/board", methods=["GET", "POST"])
def board():
    return request.values.get("answer", 1, type=int)