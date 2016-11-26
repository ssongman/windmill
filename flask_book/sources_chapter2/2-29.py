app.config['SERVER_NAME'] = 'example.com:5000'

@app.route("/board", subdomain="test")
@app.route("/board", subdomain="answer")
def board_domain_testandanswer():
    return "Test, Answer 도메인의 /board URL을 호출하셨습니다"