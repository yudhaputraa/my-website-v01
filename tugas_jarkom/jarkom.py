from flask import Flask, render_template, request, url_for, redirect

users = []

def es(teks):
    kunci = {'a': 'g', 'b': 'h', 'c': 'i', 'd': 'j', 'e': 'k', 'f': 'l',
             'g': 'm', 'h': 'n', 'i': 'o', 'j': 'p', 'k': 'q', 'l': 'r',
             'm': 's', 'n': 't', 'o': 'u', 'p': 'v', 'q': 'w', 'r': 'x',
             's': 'y', 't': 'z', 'u': 'a', 'v': 'b', 'w': 'c', 'x': 'd',
             'y': 'e', 'z': 'f'}

    teks_terenkripsi = ''
    for karakter in teks:
        if karakter.lower() in kunci:
            if karakter.isupper():
                teks_terenkripsi += kunci[karakter.lower()].upper()
            else:
                teks_terenkripsi += kunci[karakter]
        else:
            teks_terenkripsi += karakter

    return teks_terenkripsi


# Fungsi untuk memeriksa keberadaan pengguna
def is_valid_user(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return True
    return False

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html', users=users)

# Proses login
@app.route('/login', methods=['POST'])
def aksi_login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        password = es(password)

        if is_valid_user(username, password):
            return redirect(url_for('home'))
        else:
            message = f'Login gagal. Silakan coba lagi.'
    return render_template('index.html', message=message)
        
@app.route('/add_user', methods=['GET', 'POST'])
def tambah_user():
    message = ''  # Variabel untuk menyimpan pesan

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        password = es(password)

        # Pastikan username belum ada
        if any(user['username'] == username for user in users):
            message = 'Username sudah digunakan. Pilih username lain.'
        else:
            # Tambahkan pengguna baru ke dalam array
            new_user = {'username': username, 'password': password}
            users.append(new_user)
            message = f'Pengguna {username} berhasil ditambahkan!'

    return render_template('index.html', message=message)




if __name__ == '__main__':
    app.run(debug=True)

