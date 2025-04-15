inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

print("Números de Kaprekar:")

# Laço para verificar cada número no intervalo
for k in range(inicio, fim + 1):
    quadrado = str(k ** 2)  # Calcula o quadrado do número e transforma em string
    tamanho = len(str(k))  # Conta quantos dígitos tem o número original

    # Pega os últimos dígitos do quadrado (direita), de acordo com o tamanho do número original
    direita = quadrado[-tamanho:]

    # Pega os dígitos restantes (esquerda)
    esquerda = quadrado[:-tamanho]

    # Se a parte da direita for vazia ou só zeros, pula esse número
    if direita == "" or int(direita) == 0:
        continue

    # Se a parte da esquerda estiver vazia, considera como 0
    if esquerda == "":
        esquerda = "0"

    # Soma esquerda + direita e verifica se é igual ao número original
    if int(esquerda) + int(direita) == k:
        print(k)
