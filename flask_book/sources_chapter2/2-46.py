from werkzeug.datastructures import MultiDict

post = MultiDict()
post.setlist("foo", ["ham", "ham2"])
post.setlistdefault("foo2", ["answer", "answer2"])
post.clear()