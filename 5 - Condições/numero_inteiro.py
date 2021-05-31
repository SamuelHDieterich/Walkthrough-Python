# DIGITE UM NÚMERO INTEIRO

# Tenta executar as seguintes linhas
try:
    # Entrada do usuário
    num = int(input('Digite um número inteiro: '))
    print(f'O número digitado foi: {num}')

# Se a qualquer momento dentro de 'try' der um erro do tipo explícito, 
# as seguintes linhas são executadas
except ValueError:
    print('Erro de entrada')