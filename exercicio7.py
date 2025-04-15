n = int(input("Digite um número para gerar o padrão: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()
