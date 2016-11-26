from flask import Flask, Response

app = Flask(__name__)


@app.route("/")
def custom_response():
    c_response = Response("사용자 응답 테스트")

    c_response.headers.add('Program-Name', 'The Second Flask Book')

    return c_response

app.run()