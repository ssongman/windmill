from werkzeug.datastructures import MultiDict

post = MultiDict()
post.setlist("question", ["answer1", "answer2"])