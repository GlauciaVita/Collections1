idades = [15, 87, 65, 56, 32, 49, 37]

for i in range(len(idades)):
    print(i, idades[i])

for valor in enumerate(idades):
    print(valor)

for indice, idade in enumerate(idades):
    print(indice, ':', idade)

usuarios = [
    ('Aline', 35, 1987),
    ('Alice', 30, 1992),
    ('Agatha', 25, 1997)]

for nome, _, _ in usuarios:
    print(nome)

nomes = ['Aline','Alice','Agatha']
nomes_ordenados = sorted(nomes)
print(nomes_ordenados)


idades = [15, 87, 65, 56, 32, 49, 37]

idades_contrario = list(reversed(idades))
print(idades_contrario)

#igual a

idades.reverse()
print(idades)


idades_crescente = sorted(idades)
print(idades_crescente)

# igual a

idades.sort()
print(idades)


idades_crescente = sorted(idades, reverse=True)
print(idades_crescente)

#igual a

idades_contrario = list(reversed(sorted(idades)))
print(idades_contrario)


from operator import attrgetter

class ContaCorrente: 
   def __init__(self, codigo):
      self.codigo = codigo
      self.saldo = 0

   def deposita(self, valor):
      self.saldo += valor

   def __str__(self):
      return "codigo: {} saldo: {}\n".format(self.codigo, self.saldo)

conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(2500)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1800)

conta_da_aline = ContaCorrente(37)
conta_da_aline.deposita(1500)

contas = [conta_do_gui, conta_da_dani, conta_da_aline]

for conta in sorted(contas, key=attrgetter('saldo')):
   print(conta)
   
for conta in list(reversed(sorted(contas, key=attrgetter('saldo')))):
   print(conta)






















