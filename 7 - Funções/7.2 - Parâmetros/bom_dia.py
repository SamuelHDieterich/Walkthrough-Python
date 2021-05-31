# BOM DIA

# Criamos a função
# Ela recebe um parâmetro obrigatório chamado 'nome'
# Dessa forma, a partir dessa variável, podemos utilizá-la ao longo da função (sabendo que ela será um str)
def bom_dia(nome):
    "Dado um nome, retorna uma mensagem de bom dia para esse nome."
    return f'Bom dia, {nome}!'

# Passamos o argumento "Fulano" para a função (parâmetro posicional)
print(bom_dia('Fulano'))

# Podemos também definir que "nome" deve ser igual a "Ciclano"
print(bom_dia(nome='Ciclano'))