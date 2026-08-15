# ch08_10_wsgi_app.py
# Section: Server-side Programming - WSGI
# Topics: WSGI callable interface, environ, start_response
# Run with: gunicorn ch08_10_wsgi_app:application

def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"<h1>Hello, WSGI World!</h1>"]
