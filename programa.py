from random import randint
from funcoes import (
    calcula_pontos_regra_simples,
    calcula_pontos_regra_avancada,
    faz_jogada
)

def rolar_dados(n):
    return [randint(1, 6) for _ in range(n)]

def exibir_dados(dados):
    print("Dados: ", end='')
    for i, d in enumerate(dados):
        print(f"[{i}] {d} ", end='')
    print()

def imprimir_cartela(cartela):
    print("\nCartela de Pontos:")
    print("Regra Simples:")
    for i in range(1, 7):
        valor = cartela['regra_simples'][i]
        print(f"{i}: {valor if valor is not None else '-'}")
    
    print("\nRegra Avançada:")
    for nome in ['sequencia_baixa', 'sequencia_alta', 'full_house', 'quadra', 'cinco_iguais', 'sem_combinacao']:
        valor = cartela['regra_avancada'][nome]
        print(f"{nome}: {valor if valor is not None else '-'}")
    print()

def jogar_turno(cartela):
    dados = rolar_dados(5)
    exibir_dados(dados)

    for _ in range(2):  # até 2 rerrolagens
        rerrolar = input("Digite os índices dos dados que deseja rerrolar separados por espaço (ou pressione Enter para manter): ")
        if rerrolar.strip() == '':
            break

        indices = rerrolar.split()
        for i in indices:
            if i.isdigit() and int(i) in range(5):
                dados[int(i)] = randint(1, 6)
        exibir_dados(dados)

    imprimir_cartela(cartela)
    
    while True:
        categoria = input("Escolha uma categoria para marcar a pontuação (1-6 para simples ou nome da regra avançada): ")
        if categoria.isdigit():
            categoria_int = int(categoria)
            if categoria_int in cartela['regra_simples'] and cartela['regra_simples'][categoria_int] is None:
                break
        elif categoria in cartela['regra_avancada'] and cartela['regra_avancada'][categoria] is None:
            break
        print("Categoria inválida ou já preenchida. Tente novamente.")
    
    cartela = faz_jogada(dados, categoria, cartela)
    print("Jogada registrada!\n")

def main():
    cartela = {
        'regra_simples': {i: None for i in range(1, 7)},
        'regra_avancada': {
            'sequencia_baixa': None,
            'sequencia_alta': None,
            'full_house': None,
            'quadra': None,
            'cinco_iguais': None,
            'sem_combinacao': None
        }
    }

    for rodada in range(12):
        print(f"\n--- Rodada {rodada + 1} ---")
        jogar_turno(cartela)

    imprimir_cartela(cartela)
    print("Fim de jogo!")

if __name__ == "__main__":
    main()
