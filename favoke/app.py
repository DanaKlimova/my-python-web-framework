# app.py
from api import API


app = API()
# we shouldn't call the app instance, because this is gunicorn responsibility
# app()


@app.route("/home")
def home(request, response):
    response.text = "Hello from the HOME page"


@app.route("/about")
def about(request, response):
    response.text = "Hello from the ABOUT page"
