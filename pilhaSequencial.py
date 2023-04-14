class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class PilhaSequencial:
    def __init__(self) -> None:
        self.__dados = []

    def estaVazia(self) -> bool:
        return len(self.__dados) == 0

    def tamanho(self):
        return len(self.__dados)
    
    def topo(self):
        if self.estaVazia():
            raise PilhaException('A pilha está vazia')
        
        return self.__dados[0]

    def empilha(self, dado):
        self.__dados.insert(0,dado)

    def desempliha(self):
        if self.estaVazia():
            raise PilhaException('A pilha está vazia')
        
        return self.__dados.pop(0)

    def __str__(self) -> str:
        return self.__dados.__str__()
    
    def imprimir(self):
        print(self.__str__())

    