from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit-form', methods=['POST'])
def submit_form():
    nama = request.form.get('nama')
    email = request.form.get('email')

    # Simpan data ke file teks
    with open('data.txt', 'a') as file:
        file.write(f'Nama: {nama}\nEmail: {email}\n\n')

    return 'Data telah disimpan!'

if __name__ == '__main__':
    app.run()
