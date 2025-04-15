import random  # Importa a biblioteca para gerar números aleatórios

print("=== DUELO DE HERÓIS ===")

# Sorteia um valor de HP entre 200 e 1000 para ambos os jogadores
hp = random.randint(200, 1000)

# Define os status iniciais dos dois personagens
jogador_hp = hp
inimigo_hp = hp

# Sorteia ataque e defesa aleatórios entre 1 e 50 para o jogador
jogador_atk = random.randint(1, 50)
jogador_def = random.randint(1, 50)

# Sorteia ataque e defesa aleatórios entre 1 e 50 para o inimigo
inimigo_atk = random.randint(1, 50)
inimigo_def = random.randint(1, 50)

# Mostra os status iniciais na tela
print(f"Você - HP: {jogador_hp} | ATQ: {jogador_atk} | DEF: {jogador_def}")
print(f"Inimigo - HP: {inimigo_hp} | ATQ: {inimigo_atk} | DEF: {inimigo_def}")

# Começa o contador de turnos
turno = 1

# Enquanto os dois estiverem vivos, continua o jogo
while jogador_hp > 0 and inimigo_hp > 0:
    print(f"\n--- Turno {turno} ---")
    print(f"Seu HP: {jogador_hp} | Inimigo HP: {inimigo_hp}")

    # Jogador escolhe a ação
    acao = input("Sua vez - [1] Atacar | [2] Curar: ")

    # Se escolheu atacar
    if acao == "1":
        dano = max(0, jogador_atk - inimigo_def)  # Garante que o dano não seja negativo
        inimigo_hp -= dano
        print(f"Você ataca! Inimigo perdeu {dano} HP.")

    # Se escolheu curar
    elif acao == "2":
        cura = random.randint(15, 30)  # Cura aleatória entre 15 e 30
        jogador_hp += cura
        print(f"Você se curou em {cura} HP.")

    # Caso escolha inválida
    else:
        print("Opção inválida. Você perdeu o turno.")

    # Verifica se o inimigo morreu após o ataque
    if inimigo_hp <= 0:
        break

    # Ação aleatória do inimigo: atacar ou curar
    inimigo_acao = random.choice(["atacar", "curar"])

    # Se inimigo ataca
    if inimigo_acao == "atacar":
        dano = max(0, inimigo_atk - jogador_def)
        jogador_hp -= dano
        print(f"Inimigo ataca! Você perdeu {dano} HP.")

    # Se inimigo cura
    else:
        cura = random.randint(15, 30)
        inimigo_hp += cura
        print(f"Inimigo se curou em {cura} HP.")

    # Avança para o próximo turno
    turno += 1

# Mostra quem venceu no final
if jogador_hp > 0:
    print("\nVocê venceu o duelo!")
else:
    print("\nVocê perdeu o duelo!")
