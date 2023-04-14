# from pilhaSequencial import PilhaSequencial, PilhaException
from pilhaEncadeadaG import PilhaException, No, Pilha

p = Pilha()

for i in range(1, 11):
    p.empilha(i)

# p.imprimir()
print(p)

try:
    for i in range(4):
        p.desempilha()
except PilhaException as pe:
    print(pe)
p.imprimir()
print(p.topo())
# print(p.elemento(2))
# print(p.busca(6))
try:
    print('SubTopo: ',p.subTopo())
except PilhaException as pe:
    print(pe)

p.imprimir()
p.desempilha_n(2)
p.imprimir()

p2 = Pilha()
for i in range(1, 11):
    p2.empilha(i*2)
print(p2)
# p2.esvazia()
print(p2)
print(p2.obtemBase())

print('Antes da inversão: ',p2)
p2.inverte()
print('Depois da inversão: ',p2)