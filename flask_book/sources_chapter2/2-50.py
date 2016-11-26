from werkzeug.datastructures import MultiDict

post = MultiDict()
post.add("foo", "ham")

get = MultiDict()
get.add("lorem", "issue")

post.update(get)