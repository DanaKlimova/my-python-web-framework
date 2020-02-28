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


@app.route("/home/{name}")
def home(request, response, name):
    response.text = f"Hello, {name}, from the HOME page"


@app.route("/book")
class BooksResource:
    def get(self, request, response):
        response.text = "Books Page"

    def post(self, request, response):
        response.text = "Endpoint to create a book"
