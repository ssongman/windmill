from flask import Response, make_response

@app.route("/")
def response_test():
	custom_response = Response("Custom Response", '200 OK', {
		"Program": "Flask Web Application"
	})

	return make_response(custom_response)