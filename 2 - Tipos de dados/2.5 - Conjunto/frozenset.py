# A variável 'materias' recebe os valores 'matemática', 'física', 'química', 'biologia'
matérias = frozenset({'matemática', 'física', 'química', 'biologia'})

# Retorna o valor da variável
print(matérias)  # Possível retorno -->  frozenset({'química', 'biologia', 'física', 'matemática'})

# Retorna o tipo
print(type(matérias))  # <class 'frozenset'>