n = int(input("Digite o valor de n: "))

fatorial = 1

for i in range(1, n + 1):
    fatorial *= i

print(fatorial)