from source.Tokeniza import Token
from source.Arvore import *

def bot_expressao(variaveis:dict, expressao=''):
    token = Token()
    arvore = Arvore()
    if expressao == '':
        expressao = input("Escreva a expressão:\n")

        if expressao.lower() == 'exit':
            exit()

    if '=' in expressao:
        # ATRIBUIÇÃO DE VARIÁVEL
        tokens = token.tokeniza_expressao(expressao.split('=')[1], variaveis) 
        if tokens != []:
            var = expressao.split('=')[0].strip()
            if len(tokens) > 1:
                # CASO O VALOR DA VARIÁVEL SEJA UMA EXPRESSÃO ######### TESTAR AQUI
                arvore.criar_arvore(tokens)
                variaveis[var] = arvore.avaliar()
            else:
                variaveis[var] = tokens[0]
            
    elif expressao in variaveis.keys(): 
        # PRINTAR VALOR DA VARIÁVEL
        if verify_is_number(variaveis[expressao]):
            # VALOR DA VARIÁVEL É UM NÚMERO
            print(variaveis[expressao])
        
        else:
            # VALOR DA VARIÁVEL É UMA EXPRESSÃO ---- MONTAR ÁRVORE E RESOLVER ########## TESTAR AQUI
            tokens = token.tokeniza_expressao(variaveis[expressao], variaveis)  
            if tokens != []:
                arvore.criar_arvore(tokens)
                print(arvore.avaliar())

    else: 
        # EXPRESSÃO
        tokens = token.tokeniza_expressao(expressao, variaveis)  
        if tokens != []:
            arvore.criar_arvore(tokens)
            print(arvore.avaliar())


def bot_arquivo(variaveis:dict, nome_arquivo:str):
    with open(f'{nome_arquivo}.txt', 'x') as f:
        expressoes = f.readines()
        f.close()
    for expressao in expressoes:
        bot_expressao(variaveis, expressao)