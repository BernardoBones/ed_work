
def verify_is_number(char:str) -> bool:
    try:
        float(char)
        return True
    except:
        return False

class Node:
    """CRIA UM NOVO NODO"""
    # CONSTRUTOR
    def __init__(self, value, left=None, right=None) -> None:
        # SE O VALOR FOR NUMERO, CONVERTE PARA FLOAT
        self.value = float(value) if verify_is_number(value) else value

        self.left = float(left) if verify_is_number(left) else left

        self.right = float(right) if verify_is_number(right) else right 