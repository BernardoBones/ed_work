from source.Node import Node, verify_is_number

SPECIALS = '()/*-+'
OPERADORES = {'+': 0, '-': 0, '*': 1, '/': 1}
stack = []

def guarda_variavel(expressao:str, variaveis:dict):
    # for char in '()/*-+':
    #     if char in expressao:
            
    var = expressao.split('=')[0].strip()
    valor = expressao.split('=')[1].strip()
    return (var, valor)


# def calcula_expressao(expressao):



def tokeniza_expressao(expressao:str, variaveis:dict) -> list:
    temp_stack = []
    aux = 0 
    str_aux = ''
    while aux < len(expressao):   
        if expressao[aux] != ' ' and expressao[aux] not in SPECIALS: # CASO SEJA NUMERO OU LETRA
            if verify_is_number(expressao[aux]): # NUMERO
                if str_aux != '':
                    temp_stack.append(str_aux)
                    str_aux = ''  
                temp_stack.append(expressao[aux])
                aux+= 1
            else:
                # SE FOR LETRA, JUNTA NA STRING AUXILIAR
                str_aux += expressao[aux]
                aux+= 1

        elif expressao[aux] in SPECIALS:
            # CASO SEJA CARACTERE FORMADOR DE EXPRESSÃO
            if str_aux != '':
                temp_stack.append(str_aux)
                str_aux = ''
            temp_stack.append(expressao[aux])
            aux+= 1
        
        else:
            # EMPTY CHAR
            if str_aux != '':
                temp_stack.append(str_aux)
                str_aux = ''
            aux += 1
       
    # SUBSTITUI POSSÍVEIS VARIÁVEIS PELOS SEUS RESPECTIVOS VALORES
    for value in temp_stack:
        if value not in SPECIALS:
            if verify_is_number(value): # É NÚMERO
                temp_stack[temp_stack.index(value)] = float(value)
            else: # É STRING
                if value in variaveis.keys(): # EXISTE A VARIÁVEL
                    temp_stack[temp_stack.index(value)] = float(variaveis[value])
                else:
                    print(f'Erro: Variável "{value}" não inicializada')
                    exit()

    print_temp = ''
    for a in temp_stack:
        print_temp += str(a)
    print(print_temp)

    return temp_stack


def monta_subexpressao(i:int, tokens:list) -> tuple:
    """MONTA SUB EXPRESSÃO, RETORNA A RAIZ DA SUBARVORE E O INDEX DO PRÓXIMO TOKEN A SER PROCURADO"""
    sub_stack = []
    j = 1
    while j < len(tokens):
        if tokens[j] == ')':
            break
        j += 1
    sub_expressao = tokens[i+2:j]
 
    return (criar_arvore(sub_expressao, True), j)


def criar_arvore(tokens:list, subexp=False) -> Node:
    """CRIA ÁRVORE A PARTIR DA LISTA DE TOKENS, RETORNA RAIZ DA ÁRVORE"""
    i = 0
    stack = [] if subexp else stack
        
    while i < len(tokens):
        token = tokens[i]
        next_token = tokens[i+1]
        next_index = 2

        # TESTAR
        if token == '(':
            stack.append(monta_subexpressao(i, tokens))
            i+=next_index

        elif token in OPERADORES:
            try:
                left = stack.pop()
            except:
                left = tokens[i-1]
            try:
                right = stack.pop()
            except:
                if next_token == '(' :
                    right, next_index = monta_subexpressao(i, tokens)
                elif next_token == ')':
                    right = None
                else:
                    right = Node(next_token)
                    # next_index = 1
            
            stack.append(Node(token, left, right))
            
            i+= next_index  
           
        else:
            stack.append(Node(token))
            i += 1
            
    
    return stack[0]

# def avaliar_arvore(node, variaveis={}):
    # TO DO