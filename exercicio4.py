n = int(input("Insira um número inteiro para calcular o fatorial: "))

if n < 0:
    print("INVALIDO")
else:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    print(f"O fatorial de {n} é: {fatorial}")