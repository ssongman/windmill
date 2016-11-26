from flask import Flask, Response

app = Flask(__name__)

@app.route("/cookie_set")
def cookie_set():
    custom_resp = Response("Cookie를 설정합니다")
    custom_resp.set_cookie("ID", "JPUB Flask Programming")

    return custom_resp

app.run()