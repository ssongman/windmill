from flask import Flask, session
from flask.sessions import SessionInterface
from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'ext:memcached',
    'session.url': '127.0.0.1:11211',
    'session.data_dir': './cache',
}

class BeakerSessionInterface(SessionInterface):
    def open_session(self, app, request):
        session = request.environ['beaker.session']
        return session

    def save_session(self, app, session, response):
        session.save()


app = Flask(__name__)
app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)
app.session_interface = BeakerSessionInterface()


@app.route("/session_in")
def session_signin():
    if not session.has_key('test'):
        session['test'] = 'abc'
    
    return "Session Signin"

@app.route("/session_out")
def session_sighout():
    session.delete()
    return "Session Signout"

@app.route("/session_stat")
def session_stat():
    print(session["test"])
    return "Session Stat Print to Console"

app.run()