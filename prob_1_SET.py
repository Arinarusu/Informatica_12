elev1=('Popa', 'Stefan', 'M',10,10,8)
elev2=('Popescu', 'Ion', 'M',5,6,8)
elev3=('Codreanu', 'Vasile', 'M',6,9,8)
elev4=('Marinescu', 'Marius', 'M',6,7,8)
elev5=('Graur', 'Maxim', 'M',10,9,8)
print(elev1)
print(elev2)
print(elev3)
print(elev4)
print(elev5)
print('Nota medie obtinuta la sesiune de fiecare elev')
print(elev1[0:2],'Media=',sum(elev1[3::])/3)
print(elev2[0:2],'Media=',sum(elev2[3::])/3)
print(elev3[0:2],'Media=',sum(elev3[3::])/3)
print(elev4[0:2],'Media=',sum(elev4[3::])/3)
print(elev5[0:2],'Media=',sum(elev5[3::])/3)
print('Elevi restantieri')
if ((elev1[3]<5) or (elev1[4]<5) or (elev1[5]<5)):
    print(elev1[0:2])
if ((elev2[3]<5) or (elev2[4]<5) or (elev2[5]<5)):
    print(elev2[0:2])
if ((elev3[3]<5) or (elev3[4]<5) or (elev3[5]<5)):
    print(elev3[0:2])
if ((elev4[3]<5) or (elev4[4]<5) or (elev4[5]<5)):
    print(elev4[0:2])
if ((elev5[3]<5) or (elev5[4]<5) or (elev5[5]<5)):
    print(elev5[0:2])
