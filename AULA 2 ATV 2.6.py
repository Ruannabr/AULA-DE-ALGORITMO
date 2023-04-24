n = int(input("Digite até que número determinado: "))

for i in range(n+1):
    potencia = 2 ** i
    if potencia > n:
        print (f"2 elevado à {i} = {potencia}")
