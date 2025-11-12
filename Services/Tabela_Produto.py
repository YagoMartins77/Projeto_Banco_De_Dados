# Services/Produto.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS Produto(
            ID_Produto INTEGER NOT NULL PRIMARY KEY,
            Tipo_Produto TEXT NOT NULL,
            Nome_Produto TEXT NOT NULL,
            CPF_Aluno INTEGER NOT NULL,
            FOREIGN KEY (CPF_Aluno) REFERENCES Aluno (CPF_Aluno)
        );
    '''
)
cursor.close()
print("Tabela Produto criada com sucesso")