from contextlib import closing

import pymongo
from flask import Flask


DEBUG = True
SECRET_KEY = "123"
USERNAME = "admin"
PASSWORD = "admin"


app = Flask(__name__)
app.config.from_object(__name__)


def get_db():
    if not hasattr(g, "connection"):
        g.connection = pymongo.MongoClient()
    return g.connection

@teardown_request
def teardown_request(error):
    if hasattr(g, "connection"):
        g.connection.disconnect()


if __name__ == "__main__":
    app.run()
