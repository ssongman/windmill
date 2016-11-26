def redirect_new_board(adapter, id, id2):
    return "/new_board/{0}/{1}".format(id, id2)

@app.route("/board/<id>/<id2>", redirect_to=redirect_new_board)
def board(id, id2):
    return "호출되지 않을 것입니다"

@app.route("/new_board/<id>/<id2>")
def new_board(id, id2):
    return "{0}, {1} 변수와 함께 new_board URL이 호출되었습니다".format(id, id2)