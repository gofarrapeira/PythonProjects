#importa o banco
import sqlite3

#criar o banco de dados
conexao = sqlite3.connect("aula.bd")

#criar a tabela
conexao.execute("""CREATE TABLE IF NOT EXISTS ALUNO(
    ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    NOME TEXT NOT NULL,
    INDADE INT NOT NULL)""")

#INSERINDO DADOS
def insereAluno(nome, idade):
    try:
        conexao.execute("INSERT INTO ALUNO (NOME, INDADE) VALUES (?,?);", (nome, idade))
        conexao.commit
        print("Aluno inserido com sucesso")
    except sqlite3.Error as e:
        print("Erro ao inserir aluno", e)
#atualizando dados

def atualizaAluno(nomeNovo, idade, id):
    try:
        conexao.execute("UPDATE ALUNO SET NOME = ?, INDADE =? WHERE ID = ? ;", (nomeNovo, idade, id)).fetchall()
        print('Aluno atualizado com sucesso!')
    except sqlite3.Error as e:
        print("Erro ao atualizar o aluno", e)
    
#deletandoDados
def deletaAluno(id):
    try:
        conexao.execute("DELETE FROM ALUNO WHERE ID = ?;", (id,))
        print("Aluno deletado com sucesso!")
    except sqlite3.Error as e:
        print('Erro ao deletar o aluno', e)
    

#listarAlunos
def listarAlunos():
   try:
        listaAlunos =  conexao.execute("SELECT * FROM ALUNO;").fetchall()
        for aluno in listaAlunos:
            print(aluno)
   except sqlite3.Error as e:
        print("Erro ao conectar ao BD", e)
   
       
       


insereAluno("Davi","10")
insereAluno("Maria Luisa","6")
insereAluno("Bento","3")
insereAluno("LGoria","40")
listarAlunos()
atualizaAluno("Maria Luisa", "7","3")
deletaAluno("4")
listarAlunos()


