from funcoes import *

def iniciar_jogo():
    # Inicializa o estado do jogo
    cartela_jogador = {
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
    
    # Define o número máximo de rodadas
    rodadas = 12
    rerrolagens = 0
    dados_rolados = []
    dados_guardados = []

    while rodadas > 0:
        # Rola os dados no início da rodada
        dados_rolados = rolar_dados(5)
        rerrolagens = 0
        dados_guardados.clear()
        
        # Exibe os dados e opções ao jogador
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        
        while rerrolagens < 2:
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
            escolha = input("> ")

            if escolha == '1':  # Guardar um dado
                print("Digite o índice do dado a ser guardado (0 a 4):")
                indice = int(input("> "))
                if 0 <= indice < len(dados_rolados):
                    dados_guardados, dados_rolados = guardar_dado(dados_rolados, dados_guardados, indice)
                    print(f"Dados rolados: {dados_rolados}")
                    print(f"Dados guardados: {dados_guardados}")
                else:
                    print("Índice inválido. Tente novamente.")

            elif escolha == '2':  # Remover um dado
                print("Digite o índice do dado a ser removido (0 a 4):")
                indice = int(input("> "))
                if 0 <= indice < len(dados_guardados):
                    dados_guardados, dados_rolados = remover_dado(dados_rolados, dados_guardados, indice)
                    print(f"Dados rolados: {dados_rolados}")
                    print(f"Dados guardados: {dados_guardados}")
                else:
                    print("Índice inválido. Tente novamente.")
                
            elif escolha == '3':  # Rerrolar os dados
                rerrolagens += 1
                dados_rolados = rolar_dados(5 - len(dados_guardados))
                print(f"Dados rolados: {dados_rolados}")
                print(f"Dados guardados: {dados_guardados}")
                
                if rerrolagens == 2:
                    print("Você já usou todas as rerrolagens.")

            elif escolha == '4':  # Ver a cartela
                imprime_cartela(cartela_jogador)
                
            elif escolha == '0':  # Marcar a pontuação
                print("Digite a combinação desejada:")
                combinacao = input("> ")
                if combinacao in cartela_jogador['regra_simples'] and cartela_jogador['regra_simples'][int(combinacao)] == -1:
                    cartela_jogador = faz_jogada(dados_rolados, combinacao, cartela_jogador)
                elif combinacao in cartela_jogador['regra_avancada'] and cartela_jogador['regra_avancada'][combinacao] == -1:
                    cartela_jogador = faz_jogada(dados_rolados, combinacao, cartela_jogador)
                else:
                    print("Essa combinação já foi utilizada ou é inválida. Tente novamente.")
                    continue

                rodadas -= 1
                break
            else:
                print("Opção inválida. Tente novamente.")
        
        # Verifica se o jogador completou todas as rodadas
        if rodadas == 0:
            break

    # Calcula a pontuação total
    pontuacao = 0
    for valor in cartela_jogador['regra_simples'].values():
        if valor != -1:
            pontuacao += valor
    for valor in cartela_jogador['regra_avancada'].values():
        if valor != -1:
            pontuacao += valor
    
    # Verifica se o jogador tem direito ao bônus de 35 pontos
    pontos_simples = sum(p for p in cartela_jogador['regra_simples'].values() if p != -1)
    if pontos_simples >= 63:
        pontuacao += 35

    # Imprime a cartela e a pontuação final
    imprime_cartela(cartela_jogador)
    print(f"Pontuação total: {pontuacao}")

# Chama a função para iniciar o jogo
iniciar_jogo()
