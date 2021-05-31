# QUAL O MAIOR NÚMERO?

# Entrada do usuário
a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))

# if <arg> <operador> <arg>: 
if a > b:
    print(f'{a} é maior que {b}')

# Só será testado se a condição anterior for falsa
# elif <arg> <operador> <arg>: 
elif a == b:
    print(f'{a} é igual a {b}')

# 'else' não leva nenhum argumento e só será executado 
# se nenhuma condição for atendida
else:
    print(f'{a} é menor que {b}')