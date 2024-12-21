frase = input ("ingrese una frase: ")
letra = input ("ingrese una letra: ")

contador =  0
for i in frase: 
 if i == letra: 
    contador +=1

print (f"La letra {letra} se repite {contador}")

print(frase.count(letra))
