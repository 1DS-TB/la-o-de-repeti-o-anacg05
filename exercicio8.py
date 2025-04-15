n = int(input("Digite o valor de N: "))
soma = 0

for i in range(1, n + 1):           # Vai de 1 até N
    soma += 1 / i                   # Soma 1/1, 1/2, 1/3, ..., 1/N

print(f"Soma da série harmônica até {n} termos: {soma:.2f}")