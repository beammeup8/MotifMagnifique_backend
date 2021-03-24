from flask import Flask
from .user_flask import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)