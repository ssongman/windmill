app.config['SERVER_NAME'] = 'example.com:5000'

@app.route("/board", subdomain="test")
def board_domain_test():
    return "Test 도메인의 /board URL을 호출하셨습니다"

@app.route("/board", subdomain="answer")
def board_domain_answer():
    return "Answer 도메인의 /board URL을 호출하셨습니다"
