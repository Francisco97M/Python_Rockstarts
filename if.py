var = 1
hola = 'hola'
flotante = 1.34
if type(var) is int:
    print('Es un entero')
if type(hola) is str:
    print('Son letras')
if type(flotante) is float:
    print('Es flotante')
else:
    print('No es flotante')

arreglo_num = [0, 1, 2, 3]
arreglo_car = ['a', 'b', 'c', 'd']

print(arreglo_car[0])
print(arreglo_num[3])
print(len(arreglo_num))
print(arreglo_num[len(arreglo_car)-1])

for cualquiervariable in arreglo_num:
    print(cualquiervariable)