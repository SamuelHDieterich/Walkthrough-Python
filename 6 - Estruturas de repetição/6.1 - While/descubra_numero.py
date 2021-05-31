# DESCUBRA O NÚMERO

# Biblioteca
from random import randint

# Número escolhido
num = randint(1, 10) # Número aleatório entre 1 e 10
# Escolha do usuário
chute = 0

# Enquanto a escolha for diferente do número escolhido...
while chute != num:
    # Recebe uma nova tentativa do usuário
    chute = int(input('Tente adivinhar o número (entre 1 e 10):'))
    print(f'Você apostou no número {chute}')

# Parabeniza o jogador
print('Parabéns, você acertou!')