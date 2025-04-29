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