from flask import make_response

@app.route("/")
def response_test():
	return make_response(unicode("Custom Response"))