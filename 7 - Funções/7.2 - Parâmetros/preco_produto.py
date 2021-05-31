# PREÇO DE PRODUTO

# 'preço' é o parâmetro posicional
# '**kwargs' vai receber os demais parâmetros em formato de dicionário
def preço_final(preço, **kwargs):

    """
    Preço final
    -----------

    Calcula o valor final de um produto.

    args
    ----

        preço : float
        Preço inicial do produto

    **kwargs
    --------

        imposto : float
        Imposto sobre o preço (%)

        desconto : float
        Desconto sobre o preço (%)

    return
    ------

        float
        Valor final do valor do produto
    """

    # Resgata os valores do dicionário 'kwargs'
    imposto = kwargs.get('imposto')
    desconto = kwargs.get('desconto')

    # Se 'imposto' não for vazio (existir)
    if imposto:
        preço += preço * (imposto/100)

    # Se 'desconto' não for vazio (existir)
    if desconto:
        preço -= preço * (desconto/100)
    
    # Retorna o preço calculado
    return preço

valor_inicial = 80
imposto = 12.5
desconto = 5

# Mesmo não passando todas os possíveis parâmetros para **kwargs, a função ainda funciona
print(preço_final(valor_inicial, imposto = imposto, desconto = desconto))
# 85.5

# Teste mudando os valores ou comentando os parâmetros opcionais