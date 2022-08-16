animals = ['cat', 'dog', 'eel', 'bat']

print(animals[2])

fruits = [["banana", "pear", "apple"], ["lemon", "orange", "grapefruit"]]

fruits.append(["grape", "strawberry"])
fruits[-1][1]

fruits[2].insert(1, "gooseberry")

# fruits
# [['banana', 'pear', 'apple'], ['lemon', 'orange', 'grapefruit'], ['grape', 'gooseberry', 'strawberry']]
# "gooseberry" in fruits[2]
# True
# "gooseberry" not in fruits[2]
# False
# "gooseberry" not in fruits[1]
# True
for ele in fruits:
    for f in ele:
        print(f)
# create a list of
aList = list(range(0, 51, 2))

# multiple assignment
cat = ['fat', 'orange', 'cute']
size, color, personality = cat

# swap values
a ="A"
b="B"
a, b = b, a
# using a range to create a list of values starting with 1, but not including 22 with a step of 3
alist = list(range(1,22, 3))
alist
#[1, 4, 7, 10, 13, 16, 19]