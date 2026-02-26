#Diego Lipa
#Funciones

print("Hola, Juan")
print("Bienvenido al Sistema")
print("---------------------")

print("Hola, Diego")
print("Bienvenido al Sistema")
print("---------------------")

print("Hola, Pepito")
print("Bienvenido al Sistema")
print("---------------------")

lista_nombres = ["Juan", "Diego", "Pepito"]
for i in lista_nombres:
    print("Hola,",i)
    print("Bienvenido al Sistema")
    print("-----------------------------------")

print("===========================================")

def saludar(nombre):
    print("Hola,",nombre)
    print("Bienvenido al Sistema")
    print("--------------------------------------")
saludar("Juan")
saludar("Diego")
saludar("Pepito")


#Funciones con Retorno return()
def suma(primer_numero,segundo_numero):
    resultado = primer_numero + segundo_numero
    return(resultado)

print(suma(2,2))    


#Funciones sin Retorno
def suma2(primer_numero, segundo_numero):
    resultado = primer_numero + segundo_numero
    print(resultado)

suma2(2,2)
