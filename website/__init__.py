from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from sqlalchemy import inspect


# Inicializáljuk az SQLAlchemy objektumot
db = SQLAlchemy()
DB_NAME = "database.db"


# Létrehozzuk az alkalmazást
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Importáljuk a nézeteket és az auth modult
    from .views import views
    from .auth import auth

    # Importáljuk a nézeteket és az auth modult
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Importáljuk a nézeteket és az auth modult
    from .models import User, Note
    
    # Létrehozzuk az összes táblát az adatbázisban
    with app.app_context():
        db.create_all()

    # Beállítjuk a login kezelőt
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Betöltjük a felhasználót azonosító alapján
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

# Létrehozzuk az adatbázist, ha még nem létezik
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')



