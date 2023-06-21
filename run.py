# from flaskblogpost import create_app, db
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from index"

if __name__ == '__main__':
    app.run()
