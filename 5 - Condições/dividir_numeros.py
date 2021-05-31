# DIVIDIR NÚMEROS

try:
    # Entrada do usuário
    num1 = float(input('Digite o numerador: '))
    num2 = float(input('Digite o denominador: '))
    print(f'O resultado da divisão é: {num1 / num2}')

# Caso dê um erro de valor ou de interrupção via teclado
# except (<erro1>, <erro2>, ...) as <alguma coisa>:
# Assim, ele salva essa tupla de erros em uma variável
except (ValueError, KeyboardInterrupt) as erro:
    print('Erro de entrada')

# Caso o denominador seja igual a zero
except ZeroDivisionError:
    print('Não é possível dividir por zero')