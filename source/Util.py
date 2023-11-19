from source.Node import Node, verify_is_number

SPECIALS = '()/*-+'
OPERADORES = {'+': 0, '-': 0, '*': 1, '/': 1}
stack = []

def guarda_variavel(expressao:str, variaveis:dict):
    # for char in '()/*-+':
    #     if char in expressao:
            
    var = expressao.split('=')[0].strip()
    if var in variaveis.keys():
        var = variaveis[var]
    valor = expressao.split('=')[1].strip()
    return (var, valor)


def tokeniza_expressao(expressao:str, variaveis:dict) -> list:
    temp_stack = []
    aux = 0 
    str_aux = ''
    numero_aux = ''
    montar_float = ''
    
    while aux < len(expressao):   
        if expressao[aux] != ' ' and expressao[aux] not in SPECIALS: # CASO SEJA NUMERO OU LETRA
            if verify_is_number(expressao[aux]): 
                # NÚMERO
                if str_aux != '':
                    temp_stack.append(str_aux)
                    str_aux = ''  
                if montar_float != '':
                    montar_float += expressao[aux]
                    aux+=1
                else:
                    if aux < len(expressao)-1:
                        # SE NÃO FOR O ÚLTIMO CHAR
                        if expressao[aux+1] == '.':
                            # CASO O NÚMERO SEJA UM FLOAT
                            montar_float += expressao[aux]
                            montar_float += expressao[aux+1]
                            montar_float += expressao[aux+2]
                            aux+=3
                        else:
                            special = False
                            numero_aux += expressao[aux]
                            for i in range(aux+1, len(expressao)):
                                if verify_is_number(expressao[i]):
                                    numero_aux += expressao[i]
                                elif expressao[i] in SPECIALS:
                                    special = True
                                    break
                            temp_stack.append(numero_aux)
                            numero_aux = ''
                            aux = i if special else i + 1
                                
                        
                    else:
                        temp_stack.append(expressao[aux])
                        aux+= 1
                    
            else:
                if expressao[aux] in variaveis.keys():
                    # SE FOR VARIÁVEL, JÁ SUBSTITUI PELO VALOR DA VARIÁVEL
                    temp_stack.append(variaveis[expressao[aux]])
                    aux += 1
                else:
                    # SE FOR LETRA, JUNTA NA STRING AUXILIAR
                    str_aux += expressao[aux]
                    aux+= 1

        elif expressao[aux] in SPECIALS:
            # CASO SEJA CARACTERE FORMADOR DE EXPRESSÃO
            if str_aux != '':
                temp_stack.append(str_aux)
                str_aux = ''
            if montar_float != '':
                temp_stack.append(montar_float)
                montar_float = ''
            temp_stack.append(expressao[aux])
            aux+= 1

        else:
            # EMPTY CHAR
            if str_aux != '':
                temp_stack.append(str_aux)
                str_aux = ''
            if montar_float != '':
                temp_stack.append(montar_float)
                montar_float = ''
            aux += 1
       
    # SUBSTITUI POSSÍVEIS VARIÁVEIS PELOS SEUS RESPECTIVOS VALORES E CONVERTE NUMEROS PARA FLOAT
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
    if subexp: 
        stack = []
    else:
        stack = stack

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