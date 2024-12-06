import os
import json
import base64
from datetime import datetime, timedelta
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes  # type: ignore
from cryptography.hazmat.primitives import padding  # type: ignore
from utils.key_manager import KeyManager

class CustomCrypto:
    def __init__(self, key):
        self.key = key

    def encrypt(self, from_value, to_value):
        try:
            # Generate IV and salt
            iv = os.urandom(16)
            salt = os.urandom(16)
            
            # Derive key
            derived_key = KeyManager.derive_key(self.key, salt)
            
            # Create cipher
            cipher = Cipher(algorithms.AES(derived_key), modes.GCM(iv))
            encryptor = cipher.encryptor()
            
            # Combine message components
            current_time = datetime.now().isoformat()  # ISO 8601 format
            message = json.dumps({
                'from': from_value,
                'to': to_value,
                'time': current_time
            })

            # Encrypt the message
            encrypted_data = encryptor.update(message.encode()) + encryptor.finalize()
            
            # Combine components
            result = {
                'iv': base64.b64encode(iv).decode('utf-8'),
                'salt': base64.b64encode(salt).decode('utf-8'),
                'encrypted': base64.b64encode(encrypted_data).decode('utf-8'),
                'tag': base64.b64encode(encryptor.tag).decode('utf-8')
            }
            
            return base64.b64encode(json.dumps(result).encode()).decode('utf-8')
        except Exception as e:
            raise Exception(f"Encryption failed: {str(e)}")

    def decrypt(self, encrypted_data):
        try:
            # Decode and parse the encrypted data
            data = json.loads(base64.b64decode(encrypted_data))
            
            # Extract components
            iv = base64.b64decode(data['iv'])
            salt = base64.b64decode(data['salt'])
            encrypted = base64.b64decode(data['encrypted'])
            tag = base64.b64decode(data['tag'])
            
            # Derive key
            derived_key = KeyManager.derive_key(self.key, salt)
            
            # Create cipher
            cipher = Cipher(algorithms.AES(derived_key), modes.GCM(iv, tag))
            decryptor = cipher.decryptor()
            
            # Decrypt
            decrypted_message = decryptor.update(encrypted) + decryptor.finalize()
            decrypted = json.loads(decrypted_message.decode('utf-8'))

            # Check time validity (30 minutes)
            decrypted_time = datetime.fromisoformat(decrypted['time'])
            if datetime.now() - decrypted_time > timedelta(minutes=30):
                raise Exception(" Data has expired")

            return decrypted
        except Exception as e:
            raise Exception(f"Decryption failed: {str(e)}")
