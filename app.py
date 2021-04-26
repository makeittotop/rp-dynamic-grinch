from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.now()

    current_time = now.strftime("%d/%m/%y %H:%M:%S")
    return "Current Time in NZT = " + current_time
