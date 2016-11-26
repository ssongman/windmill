from flask import request

@app.route("/board")
def board():
    article_id = request.args.get("article", "1", int)
    return str(article_id)