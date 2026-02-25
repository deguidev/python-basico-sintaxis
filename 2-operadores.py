#Operadores en python

#1. Aperadores Aritméticos
suma = 5 + 5
resta = 10 - 6
multiplicacion = 5 * 5
división = 10 / 2
modulo = 10 % 6
exponente = 10 ** 2

print('El resultado de la suma es: ',suma)
print(resta)
print(multiplicacion)
print(división)
print(modulo)
print(exponente)

#2. Operadores de Comparación
print( 5 == 5 ) # Igual a
print( 5 != 5 ) # Diferente de
print( 10 > 5 ) # Mayor que
print( 10 < 5 ) # Menor que
print( 10 >= 5 ) # Mayor igual que
print( 10 <= 5 ) # Menor igual que

#3. Operadores Lógicos
v = True
f = False
 #3.1. and (y)
print('-----------------------------------AND')
print(v and v)
print(v and f)
print(f and v)
print(f and f)
 #3.2. or (o)
print('-----------------------------------OR')
print(v or v)
print(v or f)
print(f or v)
print(f or f)
 #3.3. not (negación)
print('-----------------------------------NOT')
print(not v)
print(not f)