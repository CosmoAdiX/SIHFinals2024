from flask import Flask, render_template, request, jsonify
import os
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
        message = request.json.get('message', '')
        if not message:
            raise ValueError("Message cannot be empty")
            
        encrypted = crypto.encrypt(message)
        Logger.log('Encryption', f'Message length: {len(message)}', request.remote_addr)
        return jsonify({'success': True, 'encrypted': encrypted})
    except Exception as e:
        error_msg = str(e)
        Logger.log('Encryption Error', error_msg, request.remote_addr)
        return jsonify({'success': False, 'error': error_msg}), 400

@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        encrypted = request.json.get('encrypted', '')
        if not encrypted:
            raise ValueError("Encrypted message cannot be empty")
            
        decrypted = crypto.decrypt(encrypted)
        Logger.log('Decryption', f'Message length: {len(decrypted)}', request.remote_addr)
        return jsonify({'success': True, 'decrypted': decrypted})
    except Exception as e:
        error_msg = str(e)
        Logger.log('Decryption Error', error_msg, request.remote_addr)
        return jsonify({'success': False, 'error': error_msg}), 400

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=3000)