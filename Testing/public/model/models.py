from . import db, bcrypt, login_manager  # Mengimpor db dari models/__init__.py
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Divisi(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    nama      = db.Column(db.String(100), nullable=False)
    anggota   = db.relationship('Anggota', backref='divisi_rel', lazy=True)  # Pastikan backref ada

class Anggota(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    NIM       = db.Column(db.String(20), unique=True, nullable=False)
    nama      = db.Column(db.String(100), nullable=False)
    divisi_id = db.Column(db.Integer, db.ForeignKey('divisi.id'), nullable=False)  # Pastikan ada foreign key

class User(db.Model, UserMixin) :
    __tablename__   = 'User'  # Nama tabel dalam database
    __table_args__  = {'extend_existing': True}
    id              = db.Column(db.Integer(), primary_key=True)
    username        = db.Column(db.String(30), nullable=False, unique=True)
    email           = db.Column(db.String(50), nullable=False, unique=True)
    password_hashed = db.Column(db.String(60), nullable=False)

    @property
    def password(self): 
        raise AttributeError("Password tidak bisa dibaca langsung!")

    @password.setter
    def password(self, plain_text_password):
        self.password_hashed = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hashed, attempted_password)
           


