dato = input('ingresa un dato: ')

lista = ['hola', 'adios', 'buenos dias', 'buenas noches', 'buenas tardes']

if lista.count(dato)>0:
    print('El dato (', dato, ') existe en la lista')
else:
    print('el dato (', dato, ') no existe en la lista')