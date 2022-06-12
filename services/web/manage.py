from flask.cli import FlaskGroup
from project import app, db, User


# Enables the use of cli commands to be run alongside docker-compose
# eg: docker-compose exec web python manage.py create_db
# Triggered as part of the launch of the flask app so it is set up automatically in entrypoint.sh
cli = FlaskGroup(app)


# Reset db on start up to clean state
@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


# Populate db with user(s)
@cli.command("seed_db")
def seed_db():
    db.session.add(User(email="user@company.com"))
    db.session.commit()


if __name__ == "__main__":
    cli()