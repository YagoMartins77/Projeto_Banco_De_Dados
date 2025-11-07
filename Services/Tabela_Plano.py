# Services/Tabela_Plano.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE Plano(
            Tipo_Plano VARCHAR (255) NOT NULL PRIMARY KEY,
            ID_Plano INTEGER (11) UNIQUE NOT NULL
        ) ENGINE=InnoDB;
    '''
)
cursor.close()
print("Tabela Plano criada com sucesso")