import random
n=int(input('Dati numarul de aruncari='))
nr=random.randint(1,6)
c6=0
for x in range (n):
    if nr==6:
        c6+=1
        print(nr,enf='')
        
print()
print('cifra 6 nimereste de ',c6,'ori')
