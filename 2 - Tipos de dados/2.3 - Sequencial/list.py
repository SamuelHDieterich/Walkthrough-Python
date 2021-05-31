# A variável 'y' recebe o valor 7.0 (note que não é necessário adionar o 0 depois do ponto)
y = 7. # y = float(7) 

# Retorna o valor da variável
print(y)  # 7.0

# Retorna o tipo
print(type(y))  # <class 'float'>

ficha = ['Fulano', 22, 'Masculino'] # Poderia ser: [nome, ano, sexo]
print(ficha)  # ['Fulano', 22, 'Masculino']

# Matriz identidade 3x3
matriz_I = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

print(matriz_I)  # [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Podemos retornar uma célula específica especiicando a linha e depois a coluna
print(matriz_I[1][1])  # 1