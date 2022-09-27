#password generator

import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$&£¢€¥%!"
mixer = lower_case + upper_case + numbers + symbols
password = "".join(random.sample(mixer, 20)) #length = 20

print("Your generated password is : ", password)



