# ESTADOS BRASILEIROS

# Siglas dos estados brasileiros em um 'frozenset'
estados = frozenset({
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 
    'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 
    'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 
    'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 
    'SP', 'SE', 'TO'
    })

# Entrada do usuário
resposta = str(input('Digite a sigla de um estado brasileiro: '))
resposta = resposta.upper()            # Coloca o texto em maísculo
resposta = resposta.replace(" ","")    # Tira os espaços em branco

# Verifica se a entrada do usuário está no conjunto
if resposta in estados:
    print('Muito bem! 😃')

else:
    print(f"'{resposta}' não é um estado brasileiro válido.")