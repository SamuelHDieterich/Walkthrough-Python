# DECOLAGEM - VERSÃO FOR LOOP

# Biblioteca
import time

# Mensagem inicial
print('Decolagem em:')

# Para 'i' entre 10 até 1...
for i in range(10, 0, -1):

    # Espera 1 segundo
    time.sleep(1)

    print(f'{i}...')

# Só será acionado depois que o loop acabar
print('DECOLAR!!! 🚀')