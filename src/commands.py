from flask.cli import with_appcontext
import click
from src.ext import db
from src.models import User, Activity

@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Initializing database...")
    db.drop_all()
    db.create_all()
    click.echo("Database created!")

@click.command("populate_db")
@with_appcontext
def populate_db():
    click.echo("Populating database...")



    # User
    admin = User(username="admin", role="admin")
    admin.set_password("admin123")
    db.session.add(admin)

    db.session.commit()

    click.echo("Database populated!")

