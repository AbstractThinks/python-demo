import app
import flask
main = app.create_app(__name__)

@main.route('/')
def index():
    return flask.render_template.render("index.html")
