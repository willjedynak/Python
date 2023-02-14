import math
# header
print("Name: William Jedynak")
print("ID  : 1227139214\n")
# lists to store data
fx = []
fn = []
n = 10
# initialize f(x)
for i in range(0, 21):
    if i == 5:
        fx.append(0)
    elif i == 12:
        fx.append(6)
    elif i == 20:
        fx.append(13)
    else:
        fx.append(i + 1)
# store values of pow(f(x), n)
for n in range(1, n + 1):
    for i in fx:
        fn.append(math.pow(i, n))
# create a new list and remove duplicates
lst = []
[lst.append(x) for x in fn if x not in lst]
# output relevant data
print("power value (n) is: " + str(n))
print("the count of all pow(f, n) is: " + str(len(fn)))
print("the count of distinct pow(f, n) is: " + str(len(lst)))
