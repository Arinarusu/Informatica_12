X={13,15,31,26, 73} 
Y={16, 14,42,26,87}
Z={26,54,8,9,23,31} 
stanga=not(X|Y|Z)
dreapta=(not(X))and(not(Y))and(not(Z))
if stanga==dreapta:
    print( 'Legea 1 este corecta')
else:
    print('Legea 1 este gresita')


stanga_b=not(X&Y&Z)
dreapta_b=(not(X)) | (not(Y)) | (not(Z))
if stanga_b==dreapta_b: 
    print("Legea 2 este corecta")
else: 
    print ('Legea 2 este gresita')
