# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from model import getImageUrlFrom
import os

# -- Initialization section --
app = Flask(__name__)
app.config['giphy_key'] = os.getenv('giphy_key')


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

@app.route('/yourgif', methods=['GET','POST'])

def yourgif():
    query = request.form['gifchoice']
    key=app.config['giphy_key']
    image = getImageUrlFrom(query,key)
    return render_template("yourgif.html",time = datetime.now(),image=image)