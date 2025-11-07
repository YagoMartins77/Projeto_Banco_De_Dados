# Services/Produto.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE Produto(
            ID_Produto INTEGER (11) UNIQUE NOT NULL,
            Tipo_Produto VARCHAR (255) NOT NULL,
            Nome_Produto VARCHAR (255) NOT NULL,
            CPF_Aluno INTEGER (11) UNIQUE,
            FOREIGN KEY CFP_Aluno REFERENCES Aluno(CPF_Aluno)
        ) ENGINE=InnoDB;
    '''
)
cursor.close()
print("Tabela Produto criada com sucesso")