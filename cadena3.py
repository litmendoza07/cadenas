#Leer una cadena de texto y buscar una palabra o texto

def buscar(cadena, valor):
    posicion = cadena.find(valor)
    if posicion >= 0:
        return "Se encontro el valor buscado."
    else:
        return "No se encontro el valor a buscar."

def saberSiContiene(cadena, valor):
    return valor in cadena
        
cadena = input("Dime una frase: ")
valor = input("Dime el dato a buscar: ")

print(buscar(cadena, valor))
print(saberSiContiene(cadena, valor))

