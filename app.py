from flask import Flask
from flask_migrate import Migrate

from models.Professional import db
from routes.professionalRoute import professional_bp


app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)

with app.app_context():
    db.create_all()

migrate = Migrate(app, db)
app.register_blueprint(professional_bp, url_prefix='/professionals')

@app.route('/hello')
def hello_world():  # put application's code here
    return 'Hello World!'



if __name__ == '__main__':
    app.run()
