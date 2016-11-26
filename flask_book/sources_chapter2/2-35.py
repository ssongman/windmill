from flask import request

@app.route("/board", methods=["POST"])
def board():
    article_id = request.form.get("article", "1", int)
    return str(article_id)