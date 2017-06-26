import flask

def create_app(config_name):
    app = flask.Flask(config_name)
    return app


from app.main import view
