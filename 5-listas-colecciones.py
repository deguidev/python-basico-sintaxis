#Diego Lipa
#Listas
lista = ["Diego","Lipa",25,True]
print(lista[0])
# Lista de Frutas.
lista_de_frutas = ["Naranja", "Platano", "Manzana", "Palta", "Uva"]
print(lista_de_frutas[3])

lista_de_frutas[1] = "Granada"
print(lista_de_frutas)

#Matriz
matriz = [
    [1,2,3],
    [4,6,1],
    [0,1,0]
]
print(matriz[2][2])

#lista de Números
numeros = [1,100,3,4,5,6,20,8,9,0]
print(numeros[8])
print(numeros[:3])
print(numeros[1:5])
print(numeros[::2])
print(numeros[::-1])
#Ciclo For en las Listas
for i in numeros:
    print(i*10)



#Metodos en las Listas
print("--------------------- Metodos")
lista_de_frutas = ["Naranja", "Platano", "Manzana", "Palta", "Uva"]

#agregar un nuevo dato
lista_de_frutas.append("Ciruela")
print(lista_de_frutas)

#insert = insertar un dato
lista_de_frutas.insert(2,"Pera")
print(lista_de_frutas)

#remove = borrar un dato
lista_de_frutas.remove("Uva")
print(lista_de_frutas)

#pop = para obtener o eliminar el ultimo dato
lista_de_frutas.pop()
print(lista_de_frutas)

#sort() = Ordenar las Lista
lista_de_frutas.sort()
print(lista_de_frutas)

# reverse() = revertir
lista_de_frutas.reverse()
print(lista_de_frutas)

#len() = contar datos
cantidad = len(lista_de_frutas)
print(cantidad)

#index() = encontrar el Indice
indice = lista_de_frutas.index("Naranja")
print(indice)

