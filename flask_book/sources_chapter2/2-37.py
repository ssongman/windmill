from flask import request

@app.route("/board", methods=["GET", "POST"])
def board():
    return request.values.get("question", "질문을 입력하십시오")