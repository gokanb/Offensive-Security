# import random
# chars = 'abcdefghyjklmnopqrstuvwxyz'
# chars += chars.upper()
# nums = str(1234567890)
# special_chars = "!@#$%^&*()_+<>|\?/~`=-"
# chars += nums + special_chars

# length = 16
# password = "".join(random.sample(chars, length))
# print(password)


import random
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all = lower + upper + digits + symbols 

length = 16
password = "".join(random.sample(all, length))

print(password)