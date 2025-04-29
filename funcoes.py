import random

def rolar_dados(qtd_dados):
    resultado = []
    for i in range(qtd_dados):
        dado = random.randint(1, 6)
        resultado.append(dado)
    return resultado


def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    novo_dado = dados_rolados[dado_para_guardar]
    
    # Cria novas listas 
    nova_lista_rolados = []
    for i in range(len(dados_rolados)):
        if i != dado_para_guardar:
            nova_lista_rolados.append(dados_rolados[i])
    
    nova_lista_estoque = dados_no_estoque + [novo_dado]
    
    return [nova_lista_rolados, nova_lista_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    # Valor do dado que será removido do estoque
    dado = dados_no_estoque[dado_para_remover]
    
    # Cria nova lista de estoque, sem o item no índice dado_para_remover
    nova_lista_estoque = []
    for i in range(len(dados_no_estoque)):
        if i != dado_para_remover:
            nova_lista_estoque.append(dados_no_estoque[i])
    
    # Adiciona o dado de volta aos dados rolados
    nova_lista_rolados = dados_rolados + [dado]
    
    return [nova_lista_rolados, nova_lista_estoque]