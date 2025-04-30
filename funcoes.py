import random

def rolar_dados(qtd_dados):
    resultado = []
    for i in range(qtd_dados):
        dado = random.randint(1, 6)
        resultado.append(dado)
    return resultado


def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    # Acessa o valor do dado pelo índice
    dado = dados_rolados[dado_para_guardar]
    
    # Adiciona o dado ao estoque
    dados_no_estoque.append(dado)
    
    # Remove o dado da lista de dados rolados usando o valor
    dados_rolados.remove(dado)
    
    # Retorna as listas atualizadas
    return [dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(dados):
    pontos = {i: 0 for i in range(1, 7)}  # Inicializa dicionário com 0 para cada face
    for dado in dados:
        if 1 <= dado <= 6:
            pontos[dado] += dado  # Soma o valor do dado à face correspondente
    return pontos
def calcula_pontos_soma(dados):
    total = 0
    for dado in dados:
        total += dado
    return total  # <-- errado! Sai no primeiro loop

def calcula_pontos_sequencia_baixa(dados):
    unicos = list(set(dados))  
    sequencias = [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6]
    ]
    for seq in sequencias:
        tem_sequencia = True
        for num in seq:
            if num not in unicos:
                tem_sequencia = False
                break
        if tem_sequencia:
            return 15
    return 0

def calcula_pontos_sequencia_alta(dados):
    unicos = list(set(dados))  
    sequencias = [
        [1, 2, 3, 4, 5],
        [2, 3, 4, 5, 6]
    ]
    for seq in sequencias:
        tem_sequencia = True
        for num in seq:
            if num not in unicos:
                tem_sequencia = False
                break
        if tem_sequencia:
            return 30
    return 0
