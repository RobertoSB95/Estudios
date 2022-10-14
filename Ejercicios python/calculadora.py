lista_de_operaciones = ['+', '-', '/', '*']

try:
    valor1 = float(input('ingrese un valor: '))
except:
    valor1 = 'error valor 1'

try:
    valor2 = float(input('ingrese un segundo valor: '))
except:
    valor2 = 'error valor 2'
    
try:
    operacion = input('ingrese la operacion: ')
except:
    operacion = 'operacion no encontrada'

if valor1=='error valor 1' or valor2 == 'error valor 2':
    print('numeros no validos '+valor1+' y '+valor2)
elif lista_de_operaciones.count(operacion)==0:
    print('operacion no valida')
elif operacion == '+':
    print('la suma entre ',valor1 ,' y ', valor2, ' es ', valor1+valor2)
elif operacion == '-':
    print('la resta entre ', valor1, ' y ', valor2, ' es ', valor1 - valor2)
elif operacion == '*':
    print('la multiplicacion entre ', valor1, ' y ', valor2, ' es ', valor1 * valor2)
elif operacion == '/':
    print('la divicion entre ', valor1, ' y ', valor2, ' es ', valor1 / valor2)


