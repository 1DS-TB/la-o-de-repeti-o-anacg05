n = int(input("Insira um número inteiro positivo: "))

soma = 0
i = 1

if n <= 0:
    print("INVALIDO\n")

else:
    while i <= n:
        soma += i
        i += 1

    print(f"A soma de 1 até {n} é: {soma}")