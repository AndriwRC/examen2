from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def init_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile("config.py")

    db.init_app(app)

    with app.app_context():
        from .blueprints import index, new_task

        db.create_all()

        # Register Blueprints
        app.register_blueprint(index.index_bp)
        app.register_blueprint(new_task.new_task_bp)

        return app
