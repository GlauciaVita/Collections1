class ContaCorrente: 
   def __init__(self, codigo):
      self.codigo = codigo
      self.saldo = 0

   def deposita(self, valor):
      self.saldo += valor

   def __str__(self):
      return "codigo: {} saldo: {}\n".format(self.codigo, self.saldo)
   
conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)
print(conta_do_gui)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
print(conta_da_dani)

def deposita_para_todas(contas):
   for conta in contas:
      conta.deposita(100)

contas = [conta_do_gui, conta_da_dani]
print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])

guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

usuarios = [guilherme, daniela]
print(usuarios)

usuarios.append(('Paulo', 39, 1979))
print(usuarios)

contas[1].deposita(300)

for conta in contas:
   print(conta)



















