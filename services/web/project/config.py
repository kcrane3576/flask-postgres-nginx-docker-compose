import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Database configured based on DATABASE_URL
    # Otherwise, if it is not set, it will use: sqlite://
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"
