
class Autor():
    def __init__(self, nome) -> None:
        self.nome = nome


class Livro():
    def __init__(self, titulo, autor) -> None:
        self.titulo = titulo
        self.autor  = autor
        self.emprestado = False

    def emprestaLivro(self):
        if self.emprestado == True:
            print(f'O livro está emprestado')
        else: 
            self.emprestado = True
            print(f'Pode pegar o livro  emprestado')
    
    def devolucao(self):
        if self.emprestado==True:
           self.emprestado=False
           print(f'Livro devolvido') 
    
   # def buscaLivro(self, livro):
autor1= Autor("Davi")
livro1 = Livro("Patrulha Canina", "Bento")
livro2 = Livro("Star Wars",autor1)
livro3 = Livro("A bela e a fera","Maria Luísa")

livro2.emprestaLivro()
livro2.emprestaLivro()
print(autor1.nome)
print(livro1.titulo)
