# Services/Tabela_Aula.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE Aula(
            ID_Aula INTEGER (11) NOT NULL UNIQUE PRIMARY KEY,
            Tipo_Aula VARCHAR (255) UNIQUE NOT NULL,
            CPF_Professor INTEGER (11) UNIQUE NOT NULL,
            FOREIGN KEY CPF_Professor REFERENCES Professor(CPF_Professor)
        ) ENGINE=InnoDB;
    '''
)
cursor.close()
print("Tabela Aula criada com sucesso")