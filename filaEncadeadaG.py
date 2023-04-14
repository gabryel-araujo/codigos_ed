class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class No:
    def __init__(self, carga):
        self.__carga = carga
        self.__proximo = None

    @property
    def carga(self):
        return self.__carga
    
    @property
    def proximo(self):
        return self.__proximo
    
    @carga.setter
    def carga(self, novaCarga):
        self.__carga = novaCarga

    @proximo.setter
    def proximo(self, novoNo):
        self.__proximo = novoNo
    
class Head:
    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.__tam = 0

    @property
    def inicio(self):
        return self.__inicio
    
    @property
    def final(self):
        return self.__fim
    
    @property
    def tamanho(self):
        return self.__tam
    
    @inicio.setter
    def inicio(self, novoNo):
        self.__inicio = novoNo
    
    @final.setter
    def final(self, novoNo):
        self.__fim = novoNo

    @tamanho.setter
    def tamanho(self, novoNo):
        self.__tam = novoNo


class Fila:

    def __init__(self):
        self.__head = Head()

    def estaVazia(self) -> bool:
        return self.__head.tamanho == 0

    def tamanho(self):
        return self.__head.tamanho
    
    def enfileirar(self, dado):
        no = No(dado)
        if self.estaVazia():
            self.__head.inicio = no
            self.__head.final = no
        else:
            self.__head.final.proximo = no
            self.__head.final = no
        self.__head.tamanho += 1
            
    def desenfileirar(self):
        carga = self.__head.inicio
        self.__head.inicio = self.__head.inicio.proximo
        self.__head.tamanho -= 1
        return carga
    
    def elemento(self, posicao):
        cursor = self.__head.inicio
        index = 1

        while cursor is not None:
            if index is posicao:
                return cursor.carga
            cursor = cursor.proximo
            index += 1

    def busca(self, key):
        cursor = self.__head.inicio
        index = 1

        while cursor is not None:
            if key is cursor.carga:
                return index
            cursor = cursor.proximo
            index += 1

    def __str__(self):
        s = 'Frente->[ '
        cursor = self.__head.inicio
        while(cursor != None):
            s += f'{cursor.carga}, ' 
            cursor = cursor.proximo
        return s[:-2] + ' ]<-Final'
   