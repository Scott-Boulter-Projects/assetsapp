from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv
import os


# The following code first loads the environment variables from the .dotenv file within the project directory to obtain the secret key and Uniform Resource Identifier for the SQLite database, it then utilises SQLAlchemy to connect to the database, LoginManager for authentication, and Migrate for database updates. Finally, the create app function is defined to generate an instance of the app


load_dotenv()


db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db_path = os.path.join(app.instance_path, 'site.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
