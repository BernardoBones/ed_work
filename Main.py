from source.Util import *
from source.Node import verify_is_number

def main():
    variaveis = {}
    while True:
        expressao = input()
        if expressao.lower() == 'exit':
            break
        if '=' in expressao:
            flag_expressao = False
            # ATRIBUIÇÃO DE VARIÁVEL
            for spec in SPECIALS:
                if spec in expressao: 
                    tokens = tokeniza_expressao(expressao.split('=')[1], variaveis) 
                    variaveis[var] = criar_arvore(tokens)
                    flag_expressao = True
                    break
            
            if not flag_expressao:
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
            # arvore = criar_arvore(tokens)
            # print(arvore[0])
            print(tokens)


main()
# expressao = '3.2 + 4 * (2 - 1)'
# expressao = 'x = 2 y = 3 (x + 2 * (y - 1)) / 2'
# variables = {"x": 5}
