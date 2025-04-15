n = int(input("Digite o número de termos da sequência de Fibonacci que você deseja gerar: "))

a, b = 0, 1

for _ in range(n):
    print(a)
    a, b = b, a + b
