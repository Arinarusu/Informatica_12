import random
X=set()
for i in range(5):
    numere_x=random.randint(1,200)
    X.add(numere_x)

print('X=',X)
Y=set()
for i in range(5):
    numere_y=random.randint(1,200)
    Y.add(numere_y)

print('Y=',Y)
print('X|Y=',X | Y)

if X&Y==set():
    print('X&Y=nu exista numere in intersectie')
else:
    print('X&Y=',X&Y)
print('X/Y=',X-Y)
