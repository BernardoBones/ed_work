OPERADORES = {'+': 0, '-': 0, '*': 1, '/': 1}
stack = []

class Node:
    """CRIA UM NOVO NODO"""
    # CONSTRUTOR
    def __init__(self, value, left=None, right=None) -> None:
        # CASO O VALOR SEJA PASSÍVEL DE CAST PARA FLOAT, CONVERTE, CASO NÃO SEJA, É ARMAZENADO COMO STRING
        try: 
            self.value = float(value)
        except:
            self.value = str(value)
        try:        
            self.left = float(left)
        except:
            self.left = str(left)
        try:
            self.right = float(right)
        except:
            self.right = str(right)


def tokeniza_expressao(expressao) -> list:
    expressao = expressao.replace(' ', '')
    variaveis = {}
    temp_stack = []
    aux = next_value_to_replace = 0 
    while aux < len(expressao) :
        if aux <= len(expressao)-2:
            if expressao[aux+1] == '=':
                variaveis[expressao[aux]] = expressao[aux+2] 
                aux +=3
            else:
                if expressao[aux] != ' ':
                    temp_stack.append(expressao[aux])
                    aux+=1
                else:
                    aux+= 1
        else:
            temp_stack.append(expressao[aux])
            aux+=1
    
    for value in temp_stack:
        if value not in '()/*-+':
            try:
                temp_stack[temp_stack.index(value)] = float(value)
            except:
                temp_stack[temp_stack.index(value)] = float(variaveis[value])

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
 
    return (criar_arvore(sub_expressao), j)


def criar_arvore(tokens:list) -> Node:
    """CRIA ÁRVORE A PARTIR DA LISTA DE TOKENS, RETORNA RAIZ DA ÁRVORE"""
    i = 0
    
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