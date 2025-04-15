for num in range(1, 10001):  # De 1 até 10000
    soma_divisores = 0

    for i in range(1, num):  # Verifica todos os divisores menores que o número

        if num % i == 0:
            soma_divisores += i

    if soma_divisores == num:
        print(num)
