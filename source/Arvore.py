from source.Node import *

OPERADORES = '/*-–+'

class Arvore:
    def __init__(self):
        self.root = None

    def criar_arvore(self, elementos):
        """CRIA ÁRVORE DA EXPRESSÃO"""
        self.root = self._criar_arvore_recursivo(elementos)

    def _criar_arvore_recursivo(self, elementos):
        """PERCORRE RECURSIVAMENTE OS ELEMENTOS, CRIANDO SUBÁRVORES CASO NECESSÁRIO"""
        if not elementos:
            return None
        
        current_element = elementos.pop(0)

        if current_element == "(":
            # CRIA SUBÁRVORE PROS ELEMENTOS DENTRO DOS PARÊNTESES
            subtree_root = self._criar_arvore_recursivo(elementos)
            try:
                # REMOVE O ')' CORRESPONDENTE
                elementos.pop(0)
            except:
                return('Erro: parênteses desbalanceados')
                ##### TESTAR ESSA PARTE AQ E VER COMO VOLTAR PRA MAIN
        else:
            subtree_root = Node(current_element)

        while elementos and str(elementos[0]) in OPERADORES:
            operator = elementos.pop(0)

            # CRIA SUBÁRVORE DA DIREITA
            right_child = self._criar_arvore_recursivo(elementos)

            # CRIA UM NOVO NODE PRO OPERADOR E ATUALIZA A SUBÁRVORE
            new_node = Node(operator)
            new_node.left = subtree_root
            new_node.right = right_child
            subtree_root = new_node

        return subtree_root

    def avaliar(self, node=None):
        """AVALIA A ÁRVORE"""
        if node is None:
            node = self.root

        if str(node.value) in OPERADORES:
            left_result = self.avaliar(node.left)
            right_result = self.avaliar(node.right)

            if node.value == "+":
                return left_result + right_result
            elif node.value == "-":
                return left_result - right_result
            elif node.value == "*":
                return left_result * right_result
            elif node.value == "/":
                if right_result == 0:
                    #### VER OQ RETORNAR AQUI
                    return ('Erro: Divisão por zero')
                return left_result / right_result
        else:
            # NODE É UM OPERANDO
            return float(node.value)