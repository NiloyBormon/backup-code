import random
import string

lst = []
for i in range (0,8):
    lst.append(random.randint(33,127))
for i in lst:
    print(chr(i),end="")