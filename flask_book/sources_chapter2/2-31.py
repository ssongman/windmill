@app.route("/board", redirect_to="/new_board")
def board():
    return "/board URL을 호출하셨는데 실행이 안될겁니다"
    
@app.route("/new_board")
def new_board():
    return "/new_board URL이 호출되었습니다."