from source.Tokeniza import Token
# from source.Cria import 
from source.Node import verify_is_number

def main():
    variaveis = {}
    while True:
        token = Token()
        expressao = input()
        if expressao.lower() == 'exit':
            break
        if '=' in expressao:
            # ATRIBUIÇÃO DE VARIÁVEL
            tokens = token.tokeniza_expressao(expressao.split('=')[1], variaveis) 
            if tokens != []:
                # var, valor = guarda_variavel(expressao, variaveis)
                var = expressao.split('=')[0].strip()
                # if len(tokens) > 1:
                #     # variaveis[var] = criar_arvore(tokens)
                # else:
                variaveis[var] = tokens[0]
               
        elif expressao in variaveis.keys(): 
            # PRINTAR VALOR DA VARIÁVEL
            if verify_is_number(variaveis[expressao]):
                # VALOR DA VARIÁVEL É UM NÚMERO
                print(variaveis[expressao])
            else:
                # VALOR DA VARIÁVEL É UMA EXPRESSÃO ---- MONTAR ÁRVORE # E RESOLVER
                tokens = token.tokeniza_expressao(variaveis[expressao], variaveis)  
                # if tokens != []:
                    # arvore = criar_arvore(tokens)
                    # print(arvore[0])

        else: # EXPRESSÃO
            tokens = token.tokeniza_expressao(expressao, variaveis)  
            if tokens != []:
                # arvore = criar_arvore(tokens)
                # print(arvore[0])
                print(tokens)


main()