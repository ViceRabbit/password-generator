import random
from string import ascii_letters, punctuation, digits
class password_generator:
    def __init__(self, NumOfChars):
        self.Chars = NumOfChars
    def generate(self):
        passwordtemp = ascii_letters + punctuation + digits
        password = ''.join(random.choices(passwordtemp, k=self.Chars))
        return password

instance = password_generator(100)
print(instance.generate())