from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/cookie_set")
def cookie_set():
    custom_resp = Response("Cookie를 설정합니다")
    custom_resp.set_cookie("ID", "JPUB Flask Programming")

    return custom_resp

@app.route("/cookie_out")
def cookie_out():
    custom_resp = Response("Cookie를 종료합니다")
    custom_resp.set_cookie("ID", expires=0)

    return custom_resp

@app.route("/cookie_status")
def cookie_status():
    return "ID 쿠키는 %s 값을 가지고 있습니다" % request.cookies.get('ID', '빈 문자열')

app.run()