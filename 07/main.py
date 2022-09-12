


# lista1  =   [1, 2, 3, 4]
# lista2  =   [5, 6, 7, 8]

# lista1  =   [1, "dos", 3, "cuatro"]
# lista2  =   lista1[:]
# print("------------")
# print(f"dirección: {id(lista1)}, Lista 1: {lista1}")
# print(f"dirección:  {id(lista2)}, lista 2: {lista2})")
# print("Forma correcta")


lista1  =   [0,1,2,3,4]
lista1     .append(5)
lista2  =   [5,6,7]
lista1[5:]  =   lista2 #[5,6,7]
lista1[len(lista1):]    =   lista2

print(lista1)

###### no me funciono   lista1 .append([33,44,55,66:])
print(lista1)



#insertar al inicios de la lista varios elementos (en una lista)
lista1[:99]=lista2
print(lista1)

lista1.append(lista2)
#lista1.extend(lista2)
print(lista1)



del(lista1[0])
print(lista1)


del(lista1[2:5])
print(lista1)

#insert inserta elementos o indices dentro de una lista


