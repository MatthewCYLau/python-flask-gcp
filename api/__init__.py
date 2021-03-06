from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from .db.setup import db_connect
from api.user import views as user
from api.project import views as project
from api.skill import views as skill
from api.exception.models import *

load_dotenv("config/.env")


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})
app.register_blueprint(user.bp, url_prefix="/api")
app.register_blueprint(project.bp, url_prefix="/api")
app.register_blueprint(skill.bp, url_prefix="/api")


@app.errorhandler(UnauthorizedException)
@app.errorhandler(BadRequestException)
def handle_unauthorized_exception(e):
    return e.generate_exception_response()


db_connect()


@app.route("/ping")
def ping():

    return "pong!"
