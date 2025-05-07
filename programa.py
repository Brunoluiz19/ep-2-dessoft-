from funcoes import faz_jogada, imprime_cartela, verificar_vencedor
from random import randint

def rolar_dados(n):
    return [randint(1, 6) for _ in range(n)]

def inicializar_cartela():
    return {
        'regra_simples': {i: -1 for i in range(1, 7)},
        'regra_avancada': {
            'sequencia_baixa': -1,
            'sequencia_alta': -1,
            'full_house': -1,
            'quadra': -1,
            'cinco_iguais': -1,
            'sem_combinacao': -1
        }
    }

def main():
    print("Jogo iniciado!\n")

    cartela1 = inicializar_cartela()
    cartela2 = inicializar_cartela()

    categorias = ['1', '2', '3', '4', '5', '6',
                  'sequencia_baixa', 'sequencia_alta',
                  'full_house', 'quadra', 'cinco_iguais', 'sem_combinacao']

    for i in range(len(categorias)):
        print(f"\n--- Rodada {i+1} ---")

        # Jogador 1
        dados1 = rolar_dados(5)
        print("Jogador 1 rolou:", dados1)
        
        categoria1 = categorias[i]
        if isinstance(cartela1['regra_avancada'].get(categoria1, None), int) and cartela1['regra_avancada'][categoria1] == -1:
            print("Categoria válida:", categoria1)
            cartela1 = faz_jogada(dados1, categoria1, cartela1)
        else:
            print(f"Categoria {categoria1} já foi marcada!")

        # Jogador 2
        dados2 = rolar_dados(5)
        print("Jogador 2 rolou:", dados2)
        
        categoria2 = categorias[i]
        if isinstance(cartela2['regra_avancada'].get(categoria2, None), int) and cartela2['regra_avancada'][categoria2] == -1:
            print("Categoria válida:", categoria2)
            cartela2 = faz_jogada(dados2, categoria2, cartela2)
        else:
            print(f"Categoria {categoria2} já foi marcada!")

    print("\n--- Cartela Final do Jogador 1 ---")
    imprime_cartela(cartela1)

    print("\n--- Cartela Final do Jogador 2 ---")
    imprime_cartela(cartela2)

    # Verifica e imprime o vencedor
    vencedor = verificar_vencedor(cartela1, cartela2)
    print(f"\nResultado final: {vencedor}")

main()

