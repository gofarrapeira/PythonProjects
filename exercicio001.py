lista = []
maior = 0
menor = 0
for c in range(0,5):
   lista.append(print(int(input('Digite um numero: '))))
   if c == 0:
    maior = menor = lista[c]
   else:
    if maior is None or < lista[c]:
      maior = lista[c]
    if lista[c] < menor:
      menor = lista[c] 
  
print(f'Voce digitou os valores {lista}' )
print(f'O maior valor digitado foi{maior}')
print(f'O menor valor digitado foi{menor}')

