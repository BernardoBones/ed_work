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