class Livro():
    # Método inicializador
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def informacao(self):
        print(f'O título do livro é {self.titulo} e seu autor é {self.autor}')

# Criar uma instância da classe Livro
livro1 = Livro("Orgulho e Preconceito", "Jane Austen")

# Chamar o método informacao() da instância
livro1.informacao()