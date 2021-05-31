# A variável 'telefones' guarda uma lista de nomes com os seus valores de número de telefone
telefones = {
    'Fulano'   : '(XX) XXXX-XXXX',
    'Ciclano'  : '(YY) YYYY-YYYY',
    'Beltrano' : '(ZZ) ZZZZ-ZZZZ' 
    }
# telefones = dict(Fulano = '(XX) XXXX-XXXX', Ciclano = '(YY) YYYY-YYYY', Beltrano = '(ZZ) ZZZZ-ZZZZ')

# Retorna o valor da variável
print(telefones)  # {'Fulano': '(XX) XXXX-XXXX', 'Ciclano': '(YY) YYYY-YYYY', 'Beltrano': '(ZZ) ZZZZ-ZZZZ'}

# Podemos retornar um valor do dicionário a partir dos seus índices
print(telefones['Beltrano'])  # (ZZ) ZZZZ-ZZZZ

# Retorna o tipo
print(type(telefones))  # <class 'dict'>