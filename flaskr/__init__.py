import os
from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_login import LoginManager
# from flask_moment import Moment


# login = LoginManager()
# moment = Moment()

def create_app(config_class=Config):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    if config_class is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_object(config_class)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/login')
    def login():
        return render_template('login.html')
    
    @app.route('/whatwedo')
    def whatwedo():
        return render_template('whatwedo.html')
    
    @app.route('/whoweare')
    def whoweare():
        return render_template('whoweare.html')
   
    @app.route('/wherewework')
    def wherewework():
        return render_template('wherewework.html')
    
    @app.route('/contact')
    def contact():
        return render_template('contact.html')
   
    @app.route('/register')
    def register():
        return render_template('register.html')

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)
    
    return app
