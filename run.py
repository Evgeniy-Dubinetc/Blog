# from flaskblogpost import create_app, db
#
# app = create_app()
#
# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#         app.run(debug=False)

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=False)

<<<<<<< HEAD
=======

>>>>>>> 96b4c28 (deploy return)
