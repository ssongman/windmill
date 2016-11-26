app.config['SERVER_NAME'] = 'example.com:5000'

@app.route("/board", subdomain="<user_domain>")
def board_domain_testandanswer(user_domain):
    return "{} 도메인의 /board URL을 호출하셨습니다".format(user_domain)