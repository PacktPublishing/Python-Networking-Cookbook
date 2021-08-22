import random
import string

num_upper = random.randint(1, 7)
print(f"Adding {num_upper} uppercase letters to the password")
num_lower = random.randint(1, 7)
print(f"Adding {num_lower} lowercase letters to the password")
num_digits = random.randint(1, 7)
print(f"Adding {num_digits} digits to the password")

def add_to_password(num_to_include, choices):
    temp = ""
    for i in range(num_to_include):
        temp = temp + str(random.choice(choices))
    return temp

uppers = add_to_password(num_upper, string.ascii_uppercase)
lowers = add_to_password(num_lower, string.ascii_lowercase)
numbers = add_to_password(num_digits, string.digits)
pwd = uppers + lowers + numbers

print(f"Your password is {pwd}")
