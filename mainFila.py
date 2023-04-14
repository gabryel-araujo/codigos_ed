from filaEncadeadaG import Fila, FilaException

f = Fila()
print(f.estaVazia())
print(f.tamanho())
f.enfileirar(10)
f.enfileirar(11)
f.enfileirar(12)
print(f)
print(f.elemento(10))
print(f.busca(11))
