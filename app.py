from flask import Flask
from flask import render_template

def create_app(testing: bool = True):
    app = Flask(__name__)

    @app.route("/")
    def index():
        return f"Hello world<br>Testing: {testing}"

    return app