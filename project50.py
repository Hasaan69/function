import random
import string
characters = string.ascii_letters + string.digits
password = list(random.choices(characters, k=10))
random.shuffle(password)
print("Generated password:", ''.join(password))