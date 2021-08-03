import random
import string
letter = string.ascii_lowercase
random_number = random.choice(letter)
print(random_number)

l = [1,10,2,21,3,12]
random.shuffle(l)
print