from source.Tokeniza import Token
from source.Arvore import *
import os

def bot_expressao(variaveis:dict, expressao='', from_file=False, from_gui=False) -> None:
    """
    FUNÇÃO 'PRINCIPAL'
    
    RECEBE UM DICIONÁRIO COM AS VARIÁVEIS

    BUSCA A EXPRESSÃO VIA INPUT CASO NÃO SEJA PASSADA COMO PARÂMETRO

    GUARDA A VARIÁVEL CASO A EXPRESSÃO SEJA DE VARIÁVEL

    EXIBE O RESULTADO CASO A EXPRESSÃO SEJA ARITMÉTICA
    """
    token = Token()
    arvore = Arvore()
    if expressao == '':
        expressao = input("\nEscreva a expressão:\n")

    if '=' in expressao:
        # ATRIBUIÇÃO DE VARIÁVEL
        tokens = token.tokeniza_expressao(expressao.split('=')[1], variaveis) 
        if tokens != []:
            var = expressao.split('=')[0].strip()
            if len(tokens) > 1:
                # CASO O VALOR DA VARIÁVEL SEJA UMA EXPRESSÃO
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
            # VALOR DA VARIÁVEL É UMA EXPRESSÃO
            tokens = token.tokeniza_expressao(variaveis[expressao], variaveis)  
            if tokens != []:
                arvore.criar_arvore(tokens)
                print(arvore.avaliar())

    else: 
        # EXPRESSÃO        
        tokens = token.tokeniza_expressao(expressao, variaveis)  
        if tokens != []:
            arvore.criar_arvore(tokens)
            result = arvore.avaliar()
            if not from_gui:
                print(result)
            else:
                return result
                
            if (not from_file) and (not from_gui ) and (verify_is_number(result)):
                # -- VERIFICA SE O USUÁRIO DESEJA PRINTAR A ÁRVORE DA EXPRESSÃO (APENAS CASO NÃO ESTEJA EXECUTANDO A PARTIR DE UMA ARQUIVO E CASO NÃO TENHA DADO ERRO NO AVALIAR())
                printar = input('\nDeseja printar a árvore da expressão? S ou N\n')
                printar = True if printar.lower() == 's' else False
                print('')
                if printar:
                    arvore.printar()

def bot_arquivo(variaveis:dict, file='') -> None:
    """
    LÊ O ARQUIVO, SALVANDO AS EXPRESSÕES EM UM VETOR E CHAMA A FUNÇÃO BOT_EXPRESSAO PARA CADA UMA DELAS
    """
    try:
        with open(file, 'r') as f:
            expressoes = f.readlines()
            
    except FileNotFoundError:
        print('\nArquivo não encontrado\n')
        return
    
    for expressao in expressoes:
        expressao = expressao.replace('\n', '')
        print('\n' + expressao)
        bot_expressao(variaveis, expressao, from_file=True)