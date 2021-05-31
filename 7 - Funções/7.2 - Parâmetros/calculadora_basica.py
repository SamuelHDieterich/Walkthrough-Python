# CALCULADORA BÁSICA

# Definimos que a função 'calculadora' possui dois parâmetros, 'x' e 'y'
# Por padrão, x = 1 e y = 1, dessa forma, se nenhum argumento for passado, estes srão os seus valores
def calculadora(x = 1, y = 1):
		# Docstring
    """
    Calculadora
    -----------

    Cria um dicionário com as principais operações matemáticas, dado dois números.

    args
    ----

        x : int ou float
        Primeiro número de entrada

        y : int ou float
        Segundo número de entrada
    
    return
    ------
    
        dict
        {'operação' : valor}
    """

    # Retornamos um dicionário com as operações básicas
    return {
        'soma' : x + y,
        'subtração' : x - y,
        'divisão' : x / y,
        'multiplicação' : x * y,
        'potência' : x ** y
    }

a = 3
b = 5

# 'resultado' recebe o 'return' da função 'calculadora'
resultado = calculadora(a, b)
# resultado = calculadora(x = a, y = b)

print(resultado)
# {'soma': 8, 'subtração': -2, 'divisão': 0.6, 'multiplicação': 15, 'potência': 243}


# Caso nenhum argumento seja passado, x = 1 e y = 1
print(calculadora())
# {'soma': 2, 'subtração': 0, 'divisão': 1.0, 'multiplicação': 1, 'potência': 1}