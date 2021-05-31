# MENSAGEM PARA TODOS

# 'mensagem' é um argumento posicional
# Tudo que vier depois vai se tornar uma lista salva em 'nomes'
def mensagem(mensagem, *nomes):
    "Manda uma 'mensagem' para a lista de 'nomes'"
    for i in nomes:
        print(f'{mensagem}, {i}.')

mensagem('Oi', 'Carol', 'Beatriz', 'Pedro', 'Carlos')