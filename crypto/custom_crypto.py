import os
import json
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes # type: ignore
from cryptography.hazmat.primitives import padding # type: ignore
from utils.key_manager import KeyManager

class CustomCrypto:
    def __init__(self, key):
        self.key = key

    def encrypt(self, message):
        try:
            # Generate IV and salt
            iv = os.urandom(16)
            salt = os.urandom(16)
            
            # Derive key
            derived_key = KeyManager.derive_key(self.key, salt)
            
            # Create cipher
            cipher = Cipher(algorithms.AES(derived_key), modes.GCM(iv))
            encryptor = cipher.encryptor()
            
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
            decrypted = decryptor.update(encrypted) + decryptor.finalize()
            
            return decrypted.decode('utf-8')
        except Exception as e:
            raise Exception(f"Decryption failed: {str(e)}")