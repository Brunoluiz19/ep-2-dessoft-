import random
from funcoes import rolar_dados, guardar_dado, remover_dado, faz_jogada, imprime_cartela

def iniciar_cartela():
    cartela = {
        'regra_simples': {i: -1 for i in range(1, 7)},
        'regra_avancada': {
            'sem_combinacao': -1,
            'quadra': -1,
            'full_house': -1,
            'sequencia_baixa': -1,
            'sequencia_alta': -1,
            'cinco_iguais': -1
        }
    }
    return cartela

def calcular_pontuacao_total(cartela):
    pontos_simples = sum([p for p in cartela['regra_simples'].values() if p != -1])
    pontos_avancados = sum([p for p in cartela['regra_avancada'].values() if p != -1])
    pontuacao_total = pontos_simples + pontos_avancados

    if pontos_simples >= 63:
        pontuacao_total += 35

    return pontuacao_total

def rodada(cartela):
    rerrolagens = 0
    dados_rolados = rolar_dados(5)
    dados_guardados = []

    while rerrolagens < 2:
        print(f"\nDados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")

       
        acao = input("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação: ")


        if acao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input("> "))
            if 0 <= indice < len(dados_rolados):
                dados_guardados, dados_rolados = guardar_dado(dados_rolados, dados_guardados, indice)
            else:
                print("Índice inválido. Tente novamente.")

        elif acao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input("> "))
            if 0 <= indice < len(dados_guardados):
                dados_rolados, dados_guardados = remover_dado(dados_rolados, dados_guardados, indice)
            else:
                print("Índice inválido. Tente novamente.")

        elif acao == '3':
            if rerrolagens < 2:
                dados_rolados = rolar_dados(5 - len(dados_guardados))
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif acao == '4':
            imprime_cartela(cartela)

        elif acao == '0':
            print("Digite a combinação desejada:")
            combinacao = input("> ")
            if combinacao in cartela['regra_simples'] or combinacao in cartela['regra_avancada']:
                if combinacao in cartela['regra_simples']:
                    chave = int(combinacao)
                    if cartela['regra_simples'][chave] == -1:
                        cartela = faz_jogada(dados_guardados + dados_rolados, chave, cartela)
                        break
                    else:
                        print("Essa combinação já foi utilizada.")
                elif cartela['regra_avancada'][combinacao] == -1:
                    cartela = faz_jogada(dados_guardados + dados_rolados, combinacao, cartela)
                    break
                else:
                    print("Essa combinação já foi utilizada.")
            else:
                print("Combinação inválida. Tente novamente.")

        else:
            print("Opção inválida. Tente novamente.")

    return cartela


cartela = iniciar_cartela()

for rodada_num in range(1, 13):
    print(f"\nRodada {rodada_num}")
    cartela = rodada(cartela)

pontuacao_total = calcular_pontuacao_total(cartela)
imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao_total}")
