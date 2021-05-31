# LISTA DE CHAMADA

# Lista de nomes
chamada = (
    'Ana', 'Bianca', 'Gabriel', 'Helen', 'Kevin'
)

# Enumarate retorna, respectivamente, o índice e o valor da lista 'chamada'
for índice, valor in enumerate(chamada):
    print(f'{índice + 1} - {valor}')