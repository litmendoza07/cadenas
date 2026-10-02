vector = ["j", "u", "a", "n"]
print(type(vector))

for letra in vector:
    print(letra)
    
nombre = "Juan"
print("*"*13)
for letra in nombre:
    print(letra)


print (len(vector))
print (len(nombre))

def convertirAMayusculas(texto):
    return f"{texto.upper()}"

def convertirAMinusculas(texto):
    return f"{texto.lower()}"

def capitalizar(texto):
    return f"{texto.capitalize()}"

def titulo(texto):
    return f"{texto.title()}"

def generarEmail(texto):
    nombres = texto.split()
    email = ''.join(palabra[:3].lower() for palabra in nombres)
    return f"{email}@uamv.edu.ni"

print(convertirAMayusculas(nombre))
#print(convertirAMayusculas(vector)) 
for each in vector:
    print(convertirAMayusculas(each), end="")

print()
print(convertirAMinusculas(nombre))
print(capitalizar(nombre))
print(titulo(nombre))
print(generarEmail("Jose Alfredo Baca Moreno"))
