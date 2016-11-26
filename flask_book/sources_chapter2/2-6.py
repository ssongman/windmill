from flask import make_response

@app.route("/")
def response_test():
	return make_response("Custom Response")