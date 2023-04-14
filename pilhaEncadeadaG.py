class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class No:
    def __init__(self, carga):
        self.__carga = carga
        self.__proximo = None

    def getCarga(self):
        return self.__carga

    def insereProximo(self, novoNo):
        self.__proximo = novoNo

    def getProximo(self):
        return self.__proximo

    def temProximo(self) -> bool:
        if self.__proximo is not None:
            return self.__proximo
    
    def __str__(self):
        return f'{self.__carga}'

class Pilha:

    def __init__(self):
        self.__topo = None
        self.__tamanho = 0

    def estaVazia(self) -> bool:
        return self.__topo == None

    def tamanho(self):
        return self.__tamanho
    
    def elemento(self, posicao):
        cursor = self.__topo
        topoIndex = 1
        while cursor is not None:
            if topoIndex is posicao:
                return cursor.getCarga()
            cursor = cursor.getProximo()
            topoIndex += 1

    def busca(self, key):
        cursor = self.__topo
        topoIndex = 1
        while cursor is not None:
            if cursor.getCarga() is key:
                return topoIndex
            cursor = cursor.getProximo()
            topoIndex += 1
    
    def topo(self):
        if self.__topo is not None:
            return self.__topo.getCarga()

    def empilha(self, dado):
        no = No(dado)
        no.insereProximo(self.__topo)
        self.__topo = no
        self.__tamanho += 1

    def desempilha(self):
        if self.__topo is None:
            raise PilhaException('Não foi possível desempilhar. Pilha Vazia!')
        cargaDesempilhada = self.__topo.getCarga()
        self.__topo = self.__topo.getProximo()
        self.__tamanho -= 1
        return cargaDesempilhada
    
    def imprimir(self):
        print(self.__str__())

    def __str__(self):
        s = 'Topo -> ['
        cursor = self.__topo
        while cursor is not None:
            s += f'{cursor.getCarga()}, '
            cursor = cursor.getProximo()
        s = s[:-2]
        s += ']'
        return s

# daqui pra frente serão métodos não convencionais de uma pilha. Esses métodos são referentes a lista de exercícios

    def subTopo(self):
        if self.tamanho() is 1:
            raise PilhaException('A pilha não possui sub topo!')
        return self.elemento(2)
    
    def desempilha_n(self, n):
        for i in range(n):
            self.desempilha()

    def esvazia(self):
        self.desempilha_n(self.tamanho())

    def obtemBase(self):
        return self.elemento(self.tamanho())
    
    def inverte(self):
        pilhaAux01 = Pilha()
        pilhaAux02 = Pilha()

        while self.estaVazia() is False:
            aux = self.desempilha()
            pilhaAux01.empilha(aux)
        
        while pilhaAux01.estaVazia() is False:
            aux2 = pilhaAux01.desempilha()
            pilhaAux02.empilha(aux2)

        while pilhaAux02.estaVazia() is False:
            aux3 = pilhaAux02.desempilha()
            self.empilha(aux3)
   