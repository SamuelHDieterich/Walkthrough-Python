# DECOLAGEM

# Biblioteca
import time

# Varíavel
i = 10

# Mensagem inicial
print('Decolagem em:')

# Enquanto 'i' for maior que 0...
while i > 0:

    # Espera 1 segundo
    time.sleep(1)

    print(f'{i}...')

    # A cada passagem no loop, i perde uma unidade
    i -= 1 # i = i - 1

# Só será acionado depois que o loop acabar
print('DECOLAR!!! 🚀')