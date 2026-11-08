# flask_00_wsgi.py
# Section: How a Python Web Application Runs (WSGI)
# Demonstrates: the WSGI callable interface -- environ, start_response,
#               a body made of bytes -- with no framework at all
#
# Run (no install needed; uses the standard library's reference server):
#     python flask_00_wsgi.py
#     then visit http://127.0.0.1:8000/?name=Ada
#
# Or run it under a production WSGI server:
#     macOS/Linux:  pip install gunicorn
#                   gunicorn flask_00_wsgi:application
#     Windows:      pip install waitress
#                   waitress-serve --port=8000 flask_00_wsgi:application

from urllib.parse import parse_qs
from html import escape


def application(environ, start_response):
    """A complete web application: one function, called once per request."""
    method = environ["REQUEST_METHOD"]            # "GET", "POST", ...
    path   = environ["PATH_INFO"]                 # "/", "/about", ...
    query  = parse_qs(environ.get("QUERY_STRING", ""))
    name   = query.get("name", ["World"])[0]

    body = f"<h1>Hello, {escape(name)}!</h1><p>{method} {escape(path)}</p>"
    start_response("200 OK", [("Content-Type", "text/html; charset=utf-8")])
    return [body.encode("utf-8")]                 # the body must be bytes


if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    with make_server("127.0.0.1", 8000, application) as server:
        print("Serving on http://127.0.0.1:8000  (Ctrl+C to stop)")
        server.serve_forever()
