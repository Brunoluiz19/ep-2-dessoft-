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

def calcula_pontos_full_house(dados):
    # Inicializa listas para guardar os valores únicos e suas contagens
    valores_unicos = []
    contagens = []

    # Conta quantas vezes cada número aparece
    for i in range(5):
        valor = dados[i]
        ja_existe = False

        # Verifica se o valor já está na lista de valores únicos
        for j in range(len(valores_unicos)):
            if valores_unicos[j] == valor:
                contagens[j] += 1
                ja_existe = True
                break
        
        # Se for a primeira vez que aparece, adiciona à lista
        if not ja_existe:
            valores_unicos.append(valor)
            contagens.append(1)

    # Verifica se há exatamente dois grupos: um com 3 e outro com 2
    if len(contagens) == 2:
        if (contagens[0] == 3 and contagens[1] == 2) or (contagens[0] == 2 and contagens[1] == 3):
            # Calcula a soma dos dados manualmente
            soma = 0
            for i in range(5):
                soma += dados[i]
            return soma
    
    return 0

def calcula_pontos_quadra(dados):
    valores_unicos = []
    contagens = []

    # Conta as ocorrências de cada valor
    for i in range(len(dados)):
        valor = dados[i]
        encontrado = False

        for j in range(len(valores_unicos)):
            if valores_unicos[j] == valor:
                contagens[j] += 1
                encontrado = True
                break

        if not encontrado:
            valores_unicos.append(valor)
            contagens.append(1)

    # Verifica se existe algum valor com 4 ou mais ocorrências
    for i in range(len(contagens)):
        if contagens[i] >= 4:
            # Soma todos os dados
            soma = 0
            for k in range(len(dados)):
                soma += dados[k]
            return soma
        
    return 0

def calcula_pontos_quina(dados):
    valores_unicos = []
    contagens = []

    for i in range(len(dados)):
        valor = dados[i]
        encontrado = False

        for j in range(len(valores_unicos)):
            if valores_unicos[j] == valor:
                contagens[j] += 1
                encontrado = True
                break

        if not encontrado:
            valores_unicos.append(valor)
            contagens.append(1)

    # Verifica se alguma contagem é pelo menos 5
    for i in range(len(contagens)):
        if contagens[i] >= 5:
            return 50

    return 0
def calcula_pontos_regra_avancada(dados):
    return {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados)
    }