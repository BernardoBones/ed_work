from source.Util import *
from source.Node import verify_is_number

def __main__():
    variaveis = {}
    while True:
        expressao = input()
        if expressao.lower() == 'exit':
            break
        if '=' in expressao: # ATRIBUIÇÃO DE VARIÁVEL
            var, valor = guarda_variavel(expressao, variaveis)   
            variaveis[var] = valor

        elif expressao in variaveis.keys(): # PRINTAR VALOR DA VARIÁVEL
            if verify_is_number(variaveis[expressao]):
                # VALOR DA VARIÁVEL É UM NÚMERO
                print(variaveis[expressao])
            else:
                # VALOR DA VARIÁVEL É UMA EXPRESSÃO ---- MONTAR ÁRVORE
                tokens = tokeniza_expressao(variaveis[expressao], variaveis)  
                arvore = criar_arvore(tokens)
                print(arvore[0])

        else: # EXPRESSÃO
            tokens = tokeniza_expressao(expressao, variaveis)  
            arvore = criar_arvore(tokens)
            print(arvore[0])
    

if __name__ == '__main__':
    __main__()
# expressao = '3.2 + 4 * (2 - 1)'
# expressao = 'x = 2 y = 3 (x + 2 * (y - 1)) / 2'
# variables = {"x": 5}
