from flask import Flask

app = Flask(__name__)

@app.route("/") # Decorator
def hello_world():
    return "<p>Hello, World anjay!</p>\n<h1>Hallo Saya Satria Belva</h1>"

@app.route("/testing") # Decorator
def testing():
    return """
            <table>
                <thead>
                    <tr>
                        <th>Nomor</th>
                        <th>Nama</th>
                        <th>NIM</th>
                        <th>Prodi</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>1</td>
                        <td>Satria</td>
                        <td>222410100152</td>
                        <td>Sistem Informasi</td>
                    </tr>
                    <tr>
                        <td>2</td>
                        <td>Andini</td>
                        <td>222410101077</td>
                        <td>Sistem Informasi</td>
                    </tr>
                    <tr>
                        <td>3</td>
                        <td>Safila</td>
                        <td>222410101047</td>
                        <td>Sistem Informasi</td>
                    </tr>
                    <tr>
                        <td>3</td>
                        <td>Safila</td>
                        <td>222410101047</td>
                        <td>Sistem Informasi</td>
                    </tr>
                    <tr>
                        <td>4</td>
                        <td>Taqiyyah</td>
                        <td>222410101047</td>
                        <td>Sistem Informasi</td>
                    </tr>
                    <tr>
                        <td>5</td>
                        <td>Bagus</td>
                        <td>222410101047</td>
                        <td>Sistem Informasi</td>
                    </tr>
                    <tr>
                        <td>6</td>
                        <td>Dian</td>
                        <td>222410101047</td>
                        <td>Sistem Informasi</td>
                    </tr>
                </tbody>
            </table>
        """
@app.route('/profile/<profil>') # Decorator
def profil(profil):
    return f'<h1>Account Profile</h1><br><h4>Nama Saya Adalah {profil}</h4>'