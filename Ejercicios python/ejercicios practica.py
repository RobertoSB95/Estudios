
#multiplica 2 numeros sin usar simbolo de multiplicar

a = 5
b = 2
resultado = 0

for x in range(a):
    resultado = resultado + b

print(resultado) 

#ingresa nombre y apellido y imprimelo al reves

nombre = 'roberto'
apellido = 'sanchez'

concatenacion = nombre+' '+apellido

concatenacion = concatenacion[::-1]

print(concatenacion)

#escribe una funcion que encuentre el elemento menor de una lista

lista = [6, 3, 7, 9, 10, 33, -14, 88]
menor = 'inicial'

for x in lista:
    if menor == 'inicial':
        menor = x
    else:
        if x < menor:
            menor = x
        else:
            menor = menor
print(menor)

#escribe una funcion que devuelva el volumen de una esfera por su radio

def calculaVolumen(r):
    return 4 / 3 * 3.14 * r ** 3

resultado = calculaVolumen(5)
print(resultado)

#Escriba una funcion que indique si el usuario es mayor de edad

def mayorEdad(Usuario):
    return Usuario.edad >= 18

class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
usuario1 = Usuario('roberto', 'Sanchez', 27)
usuario2 = Usuario('manuel', 'roa', 15)

resultado1 = mayorEdad(usuario1)
resultado2 = mayorEdad(usuario2)

print(resultado1, resultado2)

#Escribir una funcion que indique si un numero es par o impar

def esPar(n):
    return n % 2 == 0

numero = esPar(4)

print(numero)

#Escribe una funcion que indique cuantas vocales tiene una palabra

palabra = 'buenas tardes'
vocales = 0

for x in palabra:
    y=x.lower()
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y == 'u' else 0

print(vocales)

# escriba una aplicacion que reciba una cantidad infinita de numeros hasta
# decir basta, luego que devuelva la suma de todos los numeros

lista = []

print('ingrese numeros y para salir escriba "salir"')
while True:
    valor = input('ingrese valor: ')
    if valor == 'salir':
        break
    else:
        try:
            valor = int(valor) 
            lista.append(valor)
        except:
            print('dato no valido')
            exit()

resultado = 0
for x in lista:
    resultado += x

print(resultado)

#escriba una funcion que reciba nombre y apellido y los vaya agregando a un archivo

def agregaNombreAArchivo(nombre, apellido):
    c = open('nombreyapellido.txt', 'a')
    c.write(nombre + ' ' + apellido + '\n')
    c.close()
    
agregaNombreAArchivo('roberto', 'sanchez')
    