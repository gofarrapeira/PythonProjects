'''' Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente. '''

lista = []
valor = int(input(f'Digite um nunero:'))
lista.append(valor)
opcao= int(input(f'Deseja continuar? Digite 1 - Sim e 2 - Nao'))
if opcao==1:
    valor = int(input(f'Digite um nunero:'))
    if valor[i]==valor[i+1]:
        print(f'Valor repetido, digite outro numero')
    elif valor[i]!=valor[i+1]:  
        lista.append(valor)
if opcao==2:
    lista.sort()
    print(lista)



