@app.route('/board')
def board_list():
    board_list = models.board.query.all()