# range pode receber até 3 parâmetros

# Apenas 1 parâmetro diz que a variável vai de 0 até o valor estipulado (-1)
arr1 = range(5) # 0, 1, 2, 3, 4

# Se utilizar dois argumentos, o primeiro será o início e o segundo o fim do arranjo
arr2 = range(2, 6) # 2, 3, 4, 5

# O terceiro argumento é o espaçamento do arranjo
arr3 = range(1, 8, 2)   # 1, 3, 5, 7
arr4 = range(5, 0, -1)  # 5, 4, 3, 2, 1 

# Retorna o valor da variável
print(arr1, arr2, arr3, arr4)  # range(0, 5) range(2, 6) range(1, 8, 2) range(5, 0, -1)

# Retorna o tipo
print(type(arr1))  # <class 'range'>