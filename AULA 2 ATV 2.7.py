n = int (input ("Digite o número: "))
fatorial = 1
for i in range (1, n+1):
    if n > 0:
        fatorial *= i
        print (fatorial)
