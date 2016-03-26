from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    pass

if __name__ == '__main__':
    app.debug = True
    app.run()
