# api.py


from webob import Request, Response


class API:
    def __call__(self, environ, start_response):
        request = Request(environ)

        status = "200 OK"
        response = Response(status=status)
        response.text = "Hello, world!"
        return response(environ, start_response)
