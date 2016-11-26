from flask import make_response

@app.route("/")
def custom_response():
    return make_response(('Tuple Custom Response', 'OK', {
        'response_method': 'Tuple Response'
    }))