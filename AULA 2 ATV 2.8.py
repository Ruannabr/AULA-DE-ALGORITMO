n = int (input ("Insira o número: "))
soma = 0
for i in range (n):
    elemento = float (input ("Insira os números:"))
    soma = soma+elemento
    media = soma/n

print (f"A mé dia dos elementos é: {media}")
