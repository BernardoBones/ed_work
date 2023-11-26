def verify_is_number(char:str) -> bool:
    """RETORNA SE O CHAR É UM NÚMERO"""
    try:
        float(char)
    except ValueError:
        return False
    return True

class Node:
    """CRIA UM NOVO NODO"""
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None