from flask import Flask, g
import markdown
import os
import shelve

app = Flask(__name__)

# Connection to DB


def get_db():
    db = getattr(g, '_database', None)

    if db is None:
        db = g._database = shelve.open("devices.db")

    return db


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# The Home Route
@app.route('/')
def index():
    """Present Documentation"""
    # Open the README
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        # Read content of the file
        content = markdown_file.read()

        # Convert to HTML
        return markdown.markdown(content)

# Flask RESTful


class DeviceList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        devices = []

        for key in keys:
            device.append(shelf[key])

        return {'message': 'Success', 'data': devices}
