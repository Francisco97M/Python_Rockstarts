var = 'hola'
flotante = 123.4
num1 = 1234
num2=5678
carac = 'c'
carac2 = 'd'

bol = True
bol2 = False
bol3 = None
print (var)
print(var+carac)
print(carac+carac2)
print(bol or bol2)
print(bol and bol2)
print(not bol)
print(not bol2)
num3 = print(num1+num2)

if 10 > 5:
    print("10 es mayor que 5")
elif 10 < 5:
    print("Eso es imposible hermano")

if bol:
    print('Usamos la variable bol')

if True:
    print('Es verdadero')
if not False:
    print('La negación de falso')

var_rapida = 0
while bol != bol2:
    if var_rapida >= 10:
        bol = False
    print(var_rapida)
    var_rapida += 1

