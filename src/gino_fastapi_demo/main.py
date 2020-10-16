from fastapi import FastAPI

from .models import db


def get_app():
    app = FastAPI(title="GINO FastAPI Demo")
    db.init_app(app)
    load_modules(app)
    return app
