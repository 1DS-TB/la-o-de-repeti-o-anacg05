numero = int(input("Digite um número para verificar se ele é primo: "))

if numero < 2:
    print(f"{numero} não é um número primo.")

else:
    for i in range(2, numero):

        if numero % i == 0:
            print(f"{numero} não é um número primo.")
            break

    else:
        print(f"{numero} é um número primo.")
