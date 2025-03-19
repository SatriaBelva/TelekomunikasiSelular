import os
from flask import Flask
from routes.routes import routes  # Import blueprint
from dotenv import load_dotenv

load_dotenv() # Memuat variabel dari .env


app = Flask(__name__)
app.register_blueprint(routes)

db_path = os.path.join(app.instance_path, 'database')
os.makedirs(db_path, exist_ok=True)  # Membuat folder secara otomatis jika belum ada

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Nonaktifkan cache file statis
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/market.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

from model import db, bcrypt, login_manager

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
