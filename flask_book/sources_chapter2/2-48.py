from werkzeug.datastructures import MultiDict

post = MultiDict()
post.add("foo", "foobar")

foo_value = post.pop("foo")
if 'foo' not in post:
    print('post 변수에 더이상 foo 변수가 없습니다.')