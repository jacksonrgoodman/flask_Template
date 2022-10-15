import os
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('image_opener.html')


if __name__ == '__main__':
    app.run(debug = True)