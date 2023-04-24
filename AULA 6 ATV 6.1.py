n = int (input ("Insira a quantidade de termos: "))
fibo= []
if n == 1:
    fibo = [1]
elif n == 2:
    fibo = [1, 1]
else:
    fibo = [1, 1]
    a = 1
    b = 1
    for i in range(2, n):
        c = a + b
        fibo += [c]
        a = b
        b = c
print(fibo)
