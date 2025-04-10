from flask import Flask, render_template
from database import read_mariadb

app = Flask(__name__)

@app.route("/")
def index():
    temperatures = read_mariadb()
    return render_template("index.html", temperatures=temperatures)

def start_webserver():
    app.run(host="0.0.0.0", port=5000, debug=True)