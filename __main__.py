from Util import *

def __main__(expressao, variaveis={}):
    tokens = tokeniza_expressao(expressao) 
    arvore = criar_arvore(tokens)
    print(arvore)
    

# expressao = '3.2 + 4 * (2 - 1)'
expressao = 'x = 2 y = 3 (x + 2 * (y - 1)) / 2'
# variables = {"x": 5}
result = __main__(expressao)
print(f"Resultado: {result}")