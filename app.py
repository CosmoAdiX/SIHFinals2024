from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime
from utils.key_manager import KeyManager
from utils.logger import Logger
from crypto.custom_crypto import CustomCrypto

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24).hex()

try:
    # Initialize encryption
    key = KeyManager.load_key()
    crypto = CustomCrypto(key)
    Logger.log('System', 'Encryption service initialized successfully')
except Exception as e:
    print(f"Error initializing encryption service: {e}")
    exit(1)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    try:
        # Get input data
        from_value = request.json.get('from', '')
        to_value = request.json.get('to', '')
        if not from_value or not to_value:
            raise ValueError("From and To fields cannot be empty")

        # Encrypt the data
        encrypted = crypto.encrypt(from_value, to_value)
        Logger.log('Encryption', f'Encrypted message for {from_value} -> {to_value}', request.remote_addr)
        return jsonify({'success': True, 'encrypted': encrypted})
    except Exception as e:
        error_msg = str(e)
        Logger.log('Encryption Error', error_msg, request.remote_addr)
        return jsonify({'success': False, 'error': error_msg}), 400

@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        # Get encrypted data
        encrypted_data = request.json.get('encrypted', '')
        if not encrypted_data:
            raise ValueError("Encrypted data cannot be empty")

        # Decrypt the data
        decrypted = crypto.decrypt(encrypted_data)
        Logger.log('Decryption', f'Decrypted message: {decrypted}', request.remote_addr)
        return jsonify({'success': True, 'decrypted': decrypted})
    except Exception as e:
        error_msg = str(e)
        Logger.log('Decryption Error', error_msg, request.remote_addr)
        return jsonify({'success': False, 'error': error_msg}), 400

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=3000)