# POTÊNCIA

# Função potência
def potência(n):
    "Retorna uma função anônima que vai ser a potência de 'n'"
    return lambda a : a ** n

# Função x^2
ao_quadrado = potência(2)

# Função x^3
ao_cubo     = potência(3)

# Testa as funções
print(ao_quadrado(5))  # 25
print(ao_cubo(5))      # 125