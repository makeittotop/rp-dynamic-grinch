import os
from flask import Flask
from datetime import datetime
import geocoder


app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

@app.route("/")

def index():
    secret_key = app.config.get("SECRET_KEY")
    msg = f"SECRET_KEY = {secret_key}"
    now = datetime.now()

    current_time = now.strftime("%d/%m/%y %H:%M:%S")
    return "Current Time in " + str(geocoder.ip('me')) + " = " + current_time + ": [" + msg + "]"
