import random
import string
password = ""
char = string.ascii_letters + string.digits + string.punctuation

for i in range(8):
    password += (random.choice(char))

print("your random password is ", password)