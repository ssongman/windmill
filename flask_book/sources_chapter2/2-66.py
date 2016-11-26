from flask import Flask, Response

app = Flask(__name__)


@app.route("/")
def custom_response():
    c_response = Response("이 책은 Flask에 깊게 공부하고 싶은 이들을 위한 책입니다.")
    c_response.set_cookie("AccessLevel", "독자")

    return c_response

app.run()