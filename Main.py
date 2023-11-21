from source.Bot import * 


def main():
    variaveis = {}
    while True:
        select = input('Digite 1 para expressão/variável e 2 para ler um arquivo:\n')
        if select == '1':
            bot_expressao(variaveis)
        elif select == '2':
            file = input('Escreva o nome do arquivo sem a extensão:\n')
            bot_arquivo(variaveis, file)
        else:
            print('Comando inválido!\n')


main()