class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return 'Codigo: {} Saldo: {}'.format(self._codigo, self._saldo)
    
conta1 = ContaSalario(37)
print(conta1)

conta2 = ContaSalario(37)
print(conta2)

if conta1 == conta2:
    print('Contas iguais')
else:
    print('Contas diferentes')


    

