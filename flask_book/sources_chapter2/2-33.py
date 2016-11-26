from flask import Flask, request

@app.route("/board")
def board_list():
    return "쿼리 스트링 question 변수의 값은 {} 입니다.".format(request.args.get('question'))