class Conta: 
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def transferir(self, valor, favorecido):
        self.sacar(valor)
        favorecido.deposita(valor)

    def sacar(self, valor):
        if valor < 0:
            print('Valor tem que ser maior que 0')
        if self._saldo < valor:
            print('Saque nao permitido, saldo insuficiente! \nSaldo: {}'.format(self._saldo))
        self._saldo -= valor

    def __str__(self):
        return "codigo: {} saldo: {}\n".format(self._codigo, self._saldo)
   
class ContaCorrente(Conta):
    def passa_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_mes(self):
        self._saldo += 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    def passa_mes(self):
        self._saldo += 5

class ContaSalario(Conta):
    def passa_mes(self):
        self._saldo = self._saldo

conta10 = ContaCorrente(10)
conta10.deposita(1000)

conta20 = ContaPoupanca(20)
conta20.deposita(500)

conta30 = ContaInvestimento(30)
conta30.deposita(800)

conta40 = ContaSalario(40)
conta40.deposita(1500)

contas = [conta10, conta20, conta30, conta40]
for conta in contas:
   conta.passa_mes()
   print(conta)

print('*********************************')

conta10.transferir(100, conta20)

conta20.sacar(250)

conta30.deposita(800)

conta40.transferir(500, conta30)

contas = [conta10, conta20, conta30, conta40]
for conta in contas:
   conta.passa_mes()
   print(conta)





