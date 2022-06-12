from flask.cli import FlaskGroup
from project import app, db


cli = FlaskGroup(app)


# Enables the use of cli commands to be run alongside docker-compose
# eg: docker-compose exec web python manage.py create_db
@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()