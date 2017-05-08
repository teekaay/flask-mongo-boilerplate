from flask import Flask
from flask import render_template
from app.models import db

app = Flask(__name__)
app.config.from_object(__name__)
app.config['MONGODB_SETTINGS'] = {
    'DB': __name__
}
app.config['SECRET_KEY'] = 'SO_SECRET_WOW'
app.debug = True

db.init_app(app)

"""
Routes.
"""

@app.route('/')
def index():
    return render_template('index.html')