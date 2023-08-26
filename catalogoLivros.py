catalogoLivros =[]
livro1 ={"titulo" : "Orgulho e Preconceito", "Autor" : "Jane Austen", "Ano": 2000 }
livro2 ={"titulo" : "Razao e Sensibilidade", "Autor" : "Jane Austen", "Ano": 1995 }
livro3={'titulo' : "Abadia", "Autor": "Jane Austin", "Ano": 1993 }

catalogoLivros.append(livro1)
catalogoLivros.append(livro2)
catalogoLivros.append(livro3)

for livro in catalogoLivros:
    print(f'O titulo do livro 1 é {livro["titulo"]}, o nome do autor é {livro["Autor"]} e o ano de publicacao é {livro["Ano"]}')

# Valor que você deseja encontrar
valor_procurado = {"titulo": "Razao e Sensibilidade"}

# Procurar a chave correspondente ao valor
chave_encontrada = None
for chave, valor in enumerate(catalogoLivros):
    if valor["titulo"] == valor_procurado["titulo"]:
        chave_encontrada = chave
        break

if chave_encontrada:
    print("Chave encontrada:", chave_encontrada)
else:
    print("Chave não encontrada para o valor especificado.")





