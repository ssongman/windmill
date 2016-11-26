from flask import make_response

@app.route("/")
def custom_response():

    def application(environ, start_response):
        response_body = 'The request method was %s' % environ['REQUEST_METHOD']

        status = '200 OK'
        response_headers = [('Content-Type', 'text/plain'),
                            ('Content-Length', str(len(response_body)))]   

        start_response(status, response_headers)

        return [response_body]

    return make_response(application)