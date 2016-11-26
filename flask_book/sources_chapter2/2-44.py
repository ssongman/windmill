from werkzeug.datastructures import MultiDict

post = MultiDict()
post.add("foo", "ham")
post.setdefault("foo", "ham2")
post.setdefault("lorem", "answer")