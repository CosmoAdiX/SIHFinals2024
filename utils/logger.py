import os
import datetime

class Logger:
    LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs')
    LOG_FILE = os.path.join(LOG_DIR, 'encryption.log')

    @staticmethod
    def ensure_directory():
        """Ensure the logs directory exists with proper permissions"""
        if not os.path.exists(Logger.LOG_DIR):
            os.makedirs(Logger.LOG_DIR, mode=0o755)

    @staticmethod
    def log(event_type, message, ip='Unknown'):
        """Log encryption and decryption events"""
        try:
            Logger.ensure_directory()
            
            timestamp = datetime.datetime.now().isoformat()
            log_entry = f"[{timestamp}] IP:{ip} {event_type}: {message}\n"
            
            # Append to log file with proper permissions
            with open(Logger.LOG_FILE, 'a') as f:
                f.write(log_entry)
            
            # Ensure log file has correct permissions
            os.chmod(Logger.LOG_FILE, 0o644)
            
        except Exception as e:
            print(f"Logging error: {e}")