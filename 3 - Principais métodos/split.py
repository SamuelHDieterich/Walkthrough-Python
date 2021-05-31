frase = "Rosas são vermelhas. Violetas são azuis."
separado = frase.split() # Veja que estamos passando o método tendo primeiro definido a variável

print(separado)  # ['Rosas', 'são', 'vermelhas.', 'Violetas', 'são', 'azuis.']

poema_autopsicografia = """
O poeta é um fingidor.
Finge tão completamente
Que chega a fingir que é dor
A dor que deveras sente.

E os que lêem o que escreve,
Na dor lida sentem bem,
Não as duas que ele teve,
Mas só a que eles não têm.

E assim nas calhas da roda
Gira, a entreter a razão,
Esse comboio de corda
Que se chama o coração."""

print(poema_autopsicografia.split('.'))
# ['\nO poeta é um fingidor', '\nFinge tão completamente\nQue chega a fingir que é dor\nA dor que deveras sente', '\n\nE os que lêem o que escreve,\nNa dor lida sentem bem,\nNão as duas que ele teve,\nMas só a que eles não têm', '\n\nE assim nas calhas da roda\nGira, a entreter a razão,\nEsse comboio de corda\nQue se chama o coração', '']