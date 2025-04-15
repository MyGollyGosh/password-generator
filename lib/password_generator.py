import string
import random

class Password_generator:
    def __init__(self):
        self.used_passwords = []
    
    def generate_password(self):
        password = []
        while len(password) < 21:
            password.append(random.choice(string.ascii_letters))
            password.append(random.choice(string.punctuation))
        self.used_passwords.append(password)
        return ''.join(password)