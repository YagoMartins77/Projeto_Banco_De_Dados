# Services/Tabela_Professor.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE Professor(
            CPF_Professor INTEGER (11) UNIQUE NOT NULL PRIMARY KEY,
            RG INTEGER (11) UNIQUE NOT NULL,
            Nome VARCHAR (255) NOT NULL,
            Horários TIME NOT NULL,
            Telefone INTEGER (11) UNIQUE NOT NULL
        ) ENGINE=InnoDB;
    '''
)
cursor.close()
print("Tabela Professor criada com sucesso")