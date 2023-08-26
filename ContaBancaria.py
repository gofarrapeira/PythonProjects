class ContaBancaria():
   def __init__ (self, valorInicial):     
         self.saldo = valorInicial
   
         print(f'O saldo antes do saque era {self.saldo}')
   def deposito(self, valor):
       self.saldo = self.saldo + valor
   
   def sacar(self, valor):
     if  self.saldo<valor:
          print('Não é possivel sacar, saldo insuficiente')
     if  self.saldo>=valor:
         self.saldo = self.saldo - valor  
         print(f'Saldo depois do saque {self.saldo}')
                  
   def verificaSaldo(self): 
      print(f'O saldo da conta é {self.saldo}') 

conta1 = ContaBancaria(1000)      
conta1.deposito(200)
conta1.sacar(500)
conta1.deposito(330)
conta1.verificaSaldo()
