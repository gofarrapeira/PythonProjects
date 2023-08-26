#num = [2,5,9,1]
#num[2] =3
#num.append(7)
#num.sort()
#num.sort(reverse=True)
#print(num)
#print(f'Essa lista tem {len(num)} elementos')

valores = []
maior=0
menor=0
#valores.append(2)
#valores.append(4)
#valores.append(6)
#for v in valores:
#    print(f'{v}...', end='')
#se eu precisar mostrar a chave e o valor, usar c e v num enumetare
for cont in range(0,5):
    valores.append(int(input('Digite um valor')))
    if cont==0:
        maior = menor = valores[cont]
    else:
        if valores[cont]>maior:
            maior=valores[cont]
        if valores[cont]<menor:
            menor=valores[cont]
print(f'O maior valor digitado foi {maior}')
print(f'O menor vamor digitado foi {menor}')
for i,num in enumerate(valores):
    print(f'O valor {num} está na posicao {i}')
valores.sort()
print(valores)
#print(valores.sort(reverse=True))    
            


