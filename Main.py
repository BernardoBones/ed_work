from source.Bot import * 

def main(): 
    variaveis = {}
    while True:
        select = input('Digite 1 para expressão/variável, 2 para ler um arquivo, Exit para sair:\n')
        if select == '1':
            bot_expressao(variaveis)
        elif select == '2':
            file_name = input('\nEscreva o nome do arquivo:\n')
            bot_arquivo(variaveis, file_name)
        elif select.lower() == 'exit':
            exit()
        else:
            print('\nComando inválido!\n')


main()