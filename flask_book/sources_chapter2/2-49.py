from werkzeug.datastructures import MultiDict

post = MultiDict()
post.setlist("foo", ["ham", "ham2"])

foo_values = post.poplist("foo")
if 'foo' not in post:
    print('post 변수에 더이상 foo 변수가 없습니다.')