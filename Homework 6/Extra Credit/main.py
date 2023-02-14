from itertools import permutations

nums = [0, 1, 2, 3, 4]
l = list(permutations(range(0, 5)))

def compareElement(a, b):
    for i in range(len(a)):
        if a[i] == b[i]:
            return False
    return True

for i in range(len(l)):
    if compareElement(nums, l[i]):
        print(str(l[i]))



