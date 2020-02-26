from wsgiref.simple_server import make_server
from app import application
from middleware import Reversware

server = make_server('localhost', 8000, app=Reversware(application))
server.serve_forever()
