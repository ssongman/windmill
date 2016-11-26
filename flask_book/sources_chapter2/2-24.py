from flask import Flask

app = Flask(__name__)

@app.route("/board/<article_id>")
@app.route("/board", defaults={ "article_id": 10 })
def board(article_id):
    return "{}번 게시물을 보고 계십니다.".format(article_id)

if __name__ == "__main__":
    app.run()