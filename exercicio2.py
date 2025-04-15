n = int(input("Entre com um numero inteiro: "))

while n <= 0:
    n = int(input("Erro. Digite um número positivo: "))

soma = 0
i = 1

while i <= n:
    soma += i
    i += 1

print(f"A soma de 1 até {n} é: {soma}")