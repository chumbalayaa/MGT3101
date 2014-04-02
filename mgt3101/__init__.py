from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

#---Views
from mgt3101 import views
