# Estructura condicional
# Estructura
#if expresion logica:
#if soy de River
#else:
#else no viviria

#Ejercicio 26
'''
#Entrada
n1=int(input('Ingrese n1 : '))
n2=int(input('Ingrese n2 : '))
#Proceso
if n1 > n2:
    #rama verdadera
    print('el mayor es n1')
elif n1 == n2:
    print('n1 y n2 son iguales')
else:
    #rama falsa
    print('el mayor es n2')
    '''
'''
# Act27
# Entradas
n1=int(input('Ingrese n1 : '))
n2=int(input('Ingrese n2 : '))
n3=int(input('Ingrese n3 : '))
# Proceso
suma= n1+n2+n3
if suma > 10:
    resultado= suma / 2
else:
    resultado = suma ** 3
#Salida
print(resultado)
'''
'''
#Ejercicio 28
# Entradas
horas_trab=int(input('ingrese la cantidad de horas trabajadas:'))
turno=int(input('Ingrese su turno... 1- Diurno y 2- Nocturno: '))
# Proceso
turnoA=5234
turnoB=8057.75
if turno == 1:
    cobro=horas_trab * turnoA
    print('Su sueldo es: ',cobro)
elif turno == 2:
    cobro= horas_trab * turnoB
    print('Su sueldo es: ',cobro)
else print('Opcion NO valida:')
'''
'''
# Practica
edad=int(input('Ingrese su edad:'))
if edad >=18:
   print('Mayor')
elif edad == 18:
    print('Sigue siendo mayor')
else:
print('Menor')
'''
'''
# Practica
contra2= 2112erw
if contra2 == contraseña:
    print('Coinciden las contraseñas')
elif contra2 else = contraseña:
    print('No coinciden las contraseñas')
'''
'''
n1=int(input('Ingrese el numero :'))
n2=int(input('Ingrese el numero :'))
if,n2 == 0:
print('Error de division')
 else:
print('n1/n2')
'''
'''
if renta < 10000:
   print('5%')
elif renta > 11000 and renta < 15000:
   print('10%')
if renta == 100000 and renta == 200000
print('15%')
if renta == 200000 and renta == 350000
print('20%')
if renta == 350000 and renta == 600000
print('30%')
if renta > 600000:
print('45%')
'''
'''
tipoPizza=int(input('1- Veg y 2- No Veg'))
if tipoPizza ==1:
  print('Menu vegetariano')
  print('Ingrediente')
  print('Pimiento')
  print('Tofu')
  ingrediente= input('Ingrese un ingrediente')
  if ingrediente == 'Pimiento' or ingrediente == 'Tofu':
      print('Pizza Veg')
else:
   print('Menu No Vegetariano')
   print('Ingrediente')
   print('Peperoni')
   print('Jamon')
   print('Salmon')
   ingrediente = input('Ingrese un ingrediente')
   if ingrediente == 'Peperoni' or ingrediente == 'Jamon' or ingrediente == 'Salmon':
       print('Pizza No Veg')
   '''
# funciones
# Retorna el valor absoluto del parametro que se pase
a= -12
print('el resultado de abs es: ',abs(a))
# obtiene la conversion a binario
b=0
print('el resultado de bin es: ', bin(b))
# retornar el caracter en formato unicode
c=62
print('el resultado de chr es : ', chr(c))
#  retornar el cociente y el resto de una division
d , e= 14 , 7
cociente , resto= divmod(d,e)
print(' el cociente de la division es: ',cociente,'y el resto',resto)
# convierte una cadena de texto a decimal
f= '23.54'
print('el resultado de la funcion float es: ',float(f))
# obtiene la conversion hexadecimal
g= 124
print('el resultado de la funcion hex es: ',hex(g))
# Le pide al usuario que ingrese un string (cadena de texto)
h= input('ingrese su nombre:')
print( 'el resultado de la funcion input es:',h)
# convierte una cadena de texto a un entero
i='123'
print('el resultado de la funcion int: ',int(i))
# retorna la longitud del objeto para el parametro
j=12,23,45,13,1231
print('el resultado de la funcion len es: ', len(j))
# retorna el mayor de los parametros tomados
k,l=12,43
print('el resultado de la funcion max es: ',max(k,l))
# retorna el menor de los parametros tomados
m,n=12,43
print('el resultado de la funcion min es: ',min(m,n))
# obtiene la conversion a octal
o=124
print('el resultado de la funcion oct es: ', oct(o))
# retorna el entero unicode
p= '@'
print('el resultado de la funcion ord es: ',ord(p))
# retorna la potencia entre dos numeros
q,r=2,3
print('el resultado de la funcion pow es: ',pow(q,r))
#redondea a la cantidad de decimales que quieran
s=123,43322455554
print('el resultado de la funcion round es: ',round(s))

#convierte a cadena de texto
t=2,4,1
print('el resultado de la funcion str es: ',str(t))





