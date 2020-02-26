# app.py
from api import API


app = API()
# we shouldn't call the app instance, because this is gunicorn responsibility
# app()
