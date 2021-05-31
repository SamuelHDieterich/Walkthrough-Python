# A variável "vis" recebe a posição na memória do bytes(5)
vis = memoryview(bytes(5))

# Retorna o valor da variável
print(vis)  # Possível retorno --> <memory at 0x0000024B2DBA4D00>

# Retorna o tipo
print(type(vis))  # <class 'memoryview'>