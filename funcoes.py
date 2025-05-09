import random
def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)
    
def rolar_dados(qtd_dados):
    resultado = []
    for i in range(qtd_dados):
        dado = random.randint(1, 6)
        resultado.append(dado)
    return resultado
# Função de guardar dado ajustada
def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    if dado_para_guardar < 0 or dado_para_guardar >= len(dados_rolados):
        print("Índice inválido. Tente novamente.")
        return [dados_rolados, dados_no_estoque]
    
    dado = dados_rolados[dado_para_guardar]
    dados_no_estoque.append(dado)
    dados_rolados.remove(dado)
    
    return [dados_rolados, dados_no_estoque]

# Função de remover dado ajustada
def remover_dado(dados_rolados, dados_no_estoque, indice_para_remover):
    if indice_para_remover < 0 or indice_para_remover >= len(dados_no_estoque):
        print("Índice inválido. Tente novamente.")
        return [dados_rolados, dados_no_estoque]
    
    dado_removido = dados_no_estoque.pop(indice_para_remover)
    dados_rolados.append(dado_removido)
    
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
def calcula_pontos_soma(dados):
    soma = 0
    for valor in dados:
        soma += valor
    return soma

def calcula_pontos_regra_avancada(dados):
    return {
        'cinco_iguais': calcula_pontos_quina(dados),
        'full_house': calcula_pontos_full_house(dados),
        'quadra': calcula_pontos_quadra(dados),
        'sem_combinacao': calcula_pontos_soma(dados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados)
    }

def faz_jogada(dados, categoria, cartela_de_pontos):   
    if categoria.isdigit() and int(categoria) in cartela_de_pontos['regra_simples']:
        categoria_int = int(categoria)
        pontos_simples = calcula_pontos_regra_simples(dados)
        cartela_de_pontos['regra_simples'][categoria_int] = pontos_simples[categoria_int]
    elif categoria in cartela_de_pontos['regra_avancada']:
        pontos_avancados = calcula_pontos_regra_avancada(dados)
        cartela_de_pontos['regra_avancada'][categoria] = pontos_avancados[categoria]

    return cartela_de_pontos

