from werkzeug.datastructures import MultiDict

post = MultiDict()
post.add("foo", ["ham", "ham2"])

post_copy = post.copy()
post_deepcopy = post.deepcopy()

post_copy["foo"].extend(["ham3"])
post_deepcopy["foo"].extend(["ham4"])