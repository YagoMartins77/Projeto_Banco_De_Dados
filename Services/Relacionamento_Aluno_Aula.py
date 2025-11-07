# Services/Relacionamento_Aluno_Aula.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE Aluno_Aula(
            ID_Aula INTEGER (11) UNIQUE NOT NULL,
            CPF_Aluno INTEGER (11) UNIQUE NOT NULL,
            PRIMARY KEY (ID_Aula, CPF_Aluno),
            FOREIGN KEY ID_Aula REFERENCES Aula(ID_Aula),
            FOREIGN KEY CPF_Aluno REFERENCES Aluno(CPF_Aluno)
        ) ENGINE=InnoDB;
    '''
)
cursor.close()
print("Tabela Aluno_Aula criada com sucesso")