from flask import Flask, request, Blueprint

app = Flask(__name__)

bp = Blueprint('bp', __name__)

@bp.route("/example/blueprint", methods=["GET", "POST"])
def example_environ():
    print(request.blueprint)
    return ""

app.register_blueprint(bp)
app.run(debug=True)