import random

# Função para sortear os atributos dos jogadores
# HP entre 200 e 1000, ATQ e DEF entre 1 e 50
# Cada jogador começa com todos os itens e efeitos disponíveis

def sortear_status():
    return {
        "HP": random.randint(200, 1000),
        "ATQ": random.randint(1, 50),
        "DEF": random.randint(1, 50),
        "itens": {"força": True, "cura": True, "defesa": True, "ataque_duplo": True},
        "efeitos": {"overflow": True, "loop": True, "tela_azul": True, "cache": True},
        "status": {"tela_azul": 0, "buff": 0},
        "skip": False
    }

# Função para calcular o dano com 10% de chance de crítico (dano dobrado)
# Dano mínimo é 0 (não pode ser negativo)
def calcular_dano(atq, def_inimigo):
    critico = random.random() < 0.1
    dano = max(0, atq - def_inimigo)
    if critico:
        print("Crítico! Dano dobrado!")
        dano *= 2
    return dano

# Aplica os efeitos temporários nos jogadores por turno
def aplicar_efeitos(jogador):
    if jogador["status"]["tela_azul"] > 0:
        jogador["status"]["tela_azul"] -= 1
        jogador["DEF"] = 0
    if jogador["status"]["buff"] > 0:
        jogador["status"]["buff"] -= 1
        jogador["ATQ"] += 10
    else:
        jogador["ATQ"] -= 10 if jogador["ATQ"] > 50 else 0

# Executa o turno do jogador (atacar, curar, usar item ou usar efeito)
def turno(jogador, inimigo, nome_jogador):
    if jogador["skip"]:
        print(f"{nome_jogador} perdeu o turno (Loop Infinito).")
        jogador["skip"] = False
        return

    aplicar_efeitos(jogador)

    print(f"\n{nome_jogador}: [1] Atacar [2] Curar [3] Item [4] Efeito")
    escolha = input("Escolha: ")

    if escolha == "1":
        dano = calcular_dano(jogador["ATQ"], inimigo["DEF"])
        inimigo["HP"] -= dano
        print(f"{nome_jogador} causou {dano} de dano.")
    elif escolha == "2":
        cura = random.randint(10, 30)
        jogador["HP"] += cura
        print(f"{nome_jogador} curou {cura} de HP.")
    elif escolha == "3":
        usar_item(jogador, nome_jogador)
    elif escolha == "4":
        usar_efeito(jogador, inimigo, nome_jogador)

# Função para o jogador usar um item (cada item só pode ser usado uma vez)
def usar_item(jogador, nome):
    print("Itens: [1] Poção de Força [2] Cura Total [3] Escudo Extra [4] Ataque Duplo")
    item = input("Escolha: ")
    if item == "1" and jogador["itens"]["força"]:
        jogador["status"]["buff"] = 2
        jogador["itens"]["força"] = False
        print(f"{nome} ativou Poção de Força!")
    elif item == "2" and jogador["itens"]["cura"]:
        jogador["HP"] += 100
        jogador["itens"]["cura"] = False
        print(f"{nome} usou Cura Total!")
    elif item == "3" and jogador["itens"]["defesa"]:
        jogador["DEF"] += 20
        jogador["itens"]["defesa"] = False
        print(f"{nome} ativou Escudo Extra!")
    elif item == "4" and jogador["itens"]["ataque_duplo"]:
        jogador["ATQ"] += 20
        jogador["itens"]["ataque_duplo"] = False
        print(f"{nome} ativou Ataque Duplo!")
    else:
        print("Item já usado ou inválido.")

# Função para aplicar efeitos especiais (só podem ser usados uma vez)
def usar_efeito(jogador, inimigo, nome):
    print("Efeitos: [1] Overflow [2] Loop Infinito [3] Tela Azul [4] Cache Hit")
    efeito = input("Escolha: ")
    if efeito == "1" and jogador["efeitos"]["overflow"]:
        dano = int(inimigo["HP"] * 0.05)
        inimigo["HP"] -= dano
        jogador["efeitos"]["overflow"] = False
        print(f"{nome} ativou Overflow! Inimigo perdeu {dano} de HP.")
    elif efeito == "2" and jogador["efeitos"]["loop"]:
        inimigo["skip"] = True
        jogador["efeitos"]["loop"] = False
        print(f"{nome} ativou Loop Infinito!")
    elif efeito == "3" and jogador["efeitos"]["tela_azul"]:
        inimigo["status"]["tela_azul"] = 2
        jogador["efeitos"]["tela_azul"] = False
        print(f"{nome} ativou Tela Azul!")
    elif efeito == "4" and jogador["efeitos"]["cache"]:
        if jogador["HP"] < 0.25 * 1000:
            jogador["HP"] += int(0.3 * 1000)
            jogador["efeitos"]["cache"] = False
            print(f"{nome} ativou Cache Hit!")
        else:
            print("Cache só pode ser usado com menos de 25% do HP.")
    else:
        print("Efeito já usado ou inválido.")

# Menu principal do jogo (jogar contra CPU, multiplayer ou sair)
def menu():
    while True:
        print("\n=== DUELO DE HERÓIS ===")
        print("[1] Jogar contra CPU")
        print("[2] Dois Jogadores")
        print("[3] Sair")
        escolha = input("Escolha: ")

        if escolha == "1":
            jogar(False)
        elif escolha == "2":
            jogar(True)
        elif escolha == "3":
            break

# Função que roda o jogo completo
def jogar(multiplayer):
    jogador1 = sortear_status()
    jogador2 = sortear_status()
    jogador1["nome"] = "Você"
    jogador2["nome"] = "Inimigo" if not multiplayer else "Jogador 2"

    turno_num = 1
    while jogador1["HP"] > 0 and jogador2["HP"] > 0:
        print(f"\n--- Turno {turno_num} ---")
        print(f"{jogador1['nome']} HP: {jogador1['HP']} | {jogador2['nome']} HP: {jogador2['HP']}")
        turno(jogador1, jogador2, jogador1["nome"])
        if jogador2["HP"] <= 0:
            break
        if multiplayer:
            turno(jogador2, jogador1, jogador2["nome"])
        else:
            # Ação automática da CPU
            acao = random.choice(["1", "2"])
            print(f"Inimigo escolheu: {acao}")
            if acao == "1":
                dano = calcular_dano(jogador2["ATQ"], jogador1["DEF"])
                jogador1["HP"] -= dano
                print(f"Inimigo causou {dano} de dano.")
            else:
                cura = random.randint(10, 30)
                jogador2["HP"] += cura
                print(f"Inimigo curou {cura} de HP.")
        turno_num += 1

    # Mensagem de vitória
    vencedor = jogador1["nome"] if jogador1["HP"] > 0 else jogador2["nome"]
    print(f"\n {vencedor} venceu a batalha!\n")

# Inicia o menu do jogo
menu()



