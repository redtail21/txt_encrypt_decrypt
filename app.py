from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

# Generate a key for encryption and decryption
# You must keep this key safe. If you lose it, you won't be able to decrypt the data.
key = Fernet.generate_key()
cipher_suite = Fernet(key)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    plaintext = request.form['plaintext']
    encrypted_text = cipher_suite.encrypt(plaintext.encode()).decode()
    return render_template('index.html', encrypted_text=encrypted_text)

@app.route('/decrypt', methods=['POST'])
def decrypt():
    ciphertext = request.form['ciphertext']
    try:
        decrypted_text = cipher_suite.decrypt(ciphertext.encode()).decode()
    except Exception as e:
        decrypted_text = f"Error: {str(e)}"
    return render_template('index.html', decrypted_text=decrypted_text)

if __name__ == '__main__':
    app.run(debug=True)
