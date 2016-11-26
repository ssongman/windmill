@app.route("/board", host="example.com")
@app.route("/board", host="example2.com")
def board():
    return "/board URL을 호출하셨습니다"