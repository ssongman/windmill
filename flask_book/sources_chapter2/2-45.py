from werkzeug.datastructures import MultiDict

post = MultiDict()
post.setlist("foo", ["ham", "ham2"])
post.setlistdefault("foo", ["answer", "answer2"])