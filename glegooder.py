import pymongo
from flask import Flask


DEBUG = True
SECRET_KEY = "123"
USERNAME = "admin"
PASSWORD = "admin"


app = Flask(__name__)
app.config.from_object(__name__)


def create_mongo_db():
    return pymongo.MongoClient()


if __name__ == "__main__":
    app.run()
