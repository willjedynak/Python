print("Name: William Jedynak")
print("ID  : 1227139214")

import math

count = 100000

def sequencef(n):
    if (n <= 1):
        return n
    else:
        return sequencef(math.floor(n / 2)) + sequencef(math.floor(n / 3))

print("Value of sequencef(100000) = " + str(sequencef(count)))
