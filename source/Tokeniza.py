from source.Node import verify_is_number
import re


class Token():
    def __init__(self ) -> None:
        self.SPECIALS = '()/*-+'

    def _add_parenteses(self, chars:list) -> list:
        mult = chars.count('*')
        div = chars.count('/')
        total = 0
        parentheses_added = set()
        
        # ADD PARENTESES EM MULTIPLICAÇÕES E DIVISÕES QUE POSSUAM PRECEDÊNCIA
        while total < mult + div:
            for i in range(len(chars)):
                if chars[i] == '*' or chars[i] == '/':
                    if i not in parentheses_added:
                        try:
                            if ((chars[i - 1] != '(' and chars[i - 1] != ')') and (chars[i + 1] != '(' and chars[i + 1] != ')') 
                            and (chars[i - 2] != '(' and chars[i - 2] != ')') and (chars[i + 2] != '(' and chars[i + 2] != ')')):
                                chars.insert(i - 1, '(')
                                chars.insert(i + 3, ')')
                                parentheses_added.add(i+1)
                                total += 1
                                break
                        except IndexError:
                            try:
                                if (chars[i - 1] != '(' and chars[i - 1] != ')') and (chars[i + 1] != '(' and chars[i + 1] != ')'):
                                    chars.insert(i - 1, '(')
                                    chars.insert(i + 3, ')')
                                    parentheses_added.add(i+1)
                                    total += 1
                                    break
                            except IndexError:
                                pass
                total += 1


        # ADD PARENTESES EM ADIÇÕES E SUBTRAÇÕES QUE POSSUAM PRECEDÊNCIA
        add = chars.count('+')
        sub = chars.count('-')
        total = 0
        while total < add + sub:
            for i in range(len(chars)):
                if chars[i] == '+' or chars[i] == '-':
                    if i not in parentheses_added:
                        try:
                            if ((chars[i - 1] != '(' and chars[i - 1] != ')') and (chars[i + 1] != '(' and chars[i + 1] != ')') 
                            and (chars[i - 2] != '(' and chars[i - 2] != ')') and (chars[i + 2] != '(' and chars[i + 2] != ')')):
                                chars.insert(i - 1, '(')
                                chars.insert(i + 3, ')')
                                parentheses_added.add(i+1)
                                total += 1
                                break
                        except IndexError:
                            try:
                                if (chars[i - 1] != '(' and chars[i - 1] != ')') and (chars[i + 1] != '(' and chars[i + 1] != ')'):
                                    chars.insert(i - 1, '(')
                                    chars.insert(i + 3, ')')
                                    parentheses_added.add(i+1)
                                    total += 1
                                    break
                            except IndexError:
                                pass
                total += 1

        # JUST FOR DEBUGGING
        # print(chars)
        return chars

    def _valida_expressao(self, expressao:str) -> tuple:
        """
        VALIDA A EXPRESSÃO
        
        RETORNA TUPLA FALSE + LISTA DE CARACTERES INVÁLIDOS CASO EXISTAM,

        CASO NÃO, RETORNA TUPLA TRUE + LISTA DOS ELEMENTOS DA EXPRESSÃO
        
        """

        CHAR_PADRAO = r'[a-zA-Z0-9()+*/\-\–\s.]'

        validos = re.findall(CHAR_PADRAO, expressao)

        # VERIFICA SE TEM APENAS CHARS VALIDOS
        if ''.join(validos) == expressao:
            # FILTRA NÚMEROS E VARIÁVEIS
            PADRAO_TOP = r'\b(?:\d+\.\d+|\d+)(?:[eE][-+]?\d+)?\b|\b[a-zA-Z_]\w*\b|\S'
            
            elementos = re.findall(PADRAO_TOP, expressao)
            return (True, elementos)
        else:
            # FILTRA CARACTERES INVÁLIDOS
            invalidos = re.findall(r'[^a-zA-Z0-9()+*/\-\s.]', expressao)
            return (False, invalidos)

    def tokeniza_expressao(self, expressao:str, variaveis:dict) -> list:
        """
        'TOKENIZA' A EXPRESSÃO
        
        RETORNA LISTA COM ELEMENTOS DA EXPRESSÃO
        """

        # PRIMEIRO VALIDA A EXPRESSÃO
        resultado, chars = self._valida_expressao(expressao)
        if not resultado:
            # CASO TENHA CARACTERES INVÁLIDO
            print(f'\nErro: caracter(es) "{", ".join(chars)}" inválido(s)\n')
            return []

        # SUBSTITUI POSSÍVEIS VARIÁVEIS PELOS SEUS RESPECTIVOS VALORES E CONVERTE NUMEROS PARA FLOAT
        for value in chars:
            if value not in self.SPECIALS:
                if verify_is_number(value): # É NÚMERO
                    chars[chars.index(value)] = float(value)
                else: # É STRING
                    if value in variaveis.keys(): # EXISTE A VARIÁVEL
                        chars[chars.index(value)] = variaveis[value]
                    else:
                        print(f'\nErro: Variável "{value}" não inicializada\n')
                        return []

        return self._add_parenteses(chars)