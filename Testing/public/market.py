from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Nonaktifkan cache file statis

@app.route("/") # Decorator
@app.route('/home')
def home_page():
    return render_template('index.html')

@app.route("/testing") # Decorator
def testing():
    return render_template('tables.html')

@app.route("/market") # Decorator
def market():
    items = [
        {'nama' : 'Satria Belva Nararya', 'divisi' : 'BPH', 'NIM' : '222410101052'},
        {'nama' : 'Taqiyyah Ardelia Pratiwi', 'divisi' : 'Kaderisasi', 'NIM' : '222410101052'},
        {'nama' : 'Bagus Iman Huda', 'divisi' : 'Litbang', 'NIM' : '222410101052'},
        {'nama' : 'Safila Elsa Vavilya', 'divisi' : 'BPH', 'NIM' : '222410101052'},
        {'nama' : 'Felisita Dian Puspitasari', 'divisi' : 'BPH', 'NIM' : '222410101052'},
        {'nama' : 'Andini Niswa Nabila', 'divisi' : 'PSDM', 'NIM' : '222410101052'},
    ]
    return render_template('market.html', items=items)

@app.route("/hello") # Decorator
def hello_world():
    return "<p>Hello, World anjay!</p>\n<h1>Hallo Saya Satria Belva</h1>"

@app.route('/profile/<profil>') # Decorator
def profil(profil):
    return f'<h1><i>Account Profile</i></h1><h4>Nama Saya Adalah {profil}</h4>'

if __name__ == '__main__':
    app.run(debug=True)