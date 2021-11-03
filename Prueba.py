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

gen = (i for i in range(10) if i%2!=0)
for x in gen:
    print(x)

arreglo_num = [0, 1, 2, 3]
arreglo_num.append(4)
arreglo_num.extend([5, 6])
print(arreglo_num)

tupla = (1, 2, 3)
print(tupla)

comp = [i+1 for i in range(100) if i%2!=0]
comp.append(101)
print(comp)

dic = {'color': 'red', 'size': 123, 'width': 405.60}
for key in dic:
    print(key)
    print(dic[key])

if 'color' in dic:
    print(dic['color'])

def multiplicacion(a1,a2):
    return a1 * a2

def mult(a1,a2, i = 0, acu=0):
    if i < a2:
        return mult(a1,a2,i+1,a1+acu)
    else:
        return acu
print(multiplicacion(2,6))

print(mult(2,6))

def mult2(*args):
    res = 1
    for i in args:
        res *= i

    return res
print(mult2(2,6))
print(mult2(2,6,4,3))

def mult3(**kwargs):
    res = 1
    for key in kwargs:
        print(key)
        res *= kwargs[key]

    return res    

print(mult3(num1 = 2, num2 = 6))
print(mult3(num1 = 2, num2 = 6, num3 = 4, num4 = 3))

def mult4(*args, **kwargs):
    res = 1
    for key in kwargs:
        print(key)
        res *= kwargs[key]
    
    for i in args:
        res *= i

    return

print(mult4(4, 3, num1 = 2, num2 = 6))