from flask import Flask, Response

app = Flask(__name__)


@app.route("/")
def custom_response():
    c_response = Response("사용자 응답 테스트")

    c_response.headers.add('Program-Name', 'The Second Flask Book')
    c_response.set_data("이 책은 Flask에 깊게 공부하고 싶은 이들을 위한 책입니다.")

    return c_response

app.run()