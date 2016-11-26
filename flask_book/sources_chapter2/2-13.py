app = Flask(__name__)
app.wsgi_app = LogMiddleware(app.wsgi_app)