# Services/Tabela_Maquina.py

import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE Maquina(
            Nome_Maquina VARCHAR (255) UNIQUE NOT NULL PRIMARY KEY,
            ID_Maquina INTEGER (11) UNIQUE NOT NULL,
            Parte_Trabalhada VARCHAR (255) NOT NULL
        ) ENGINE=InnoDB;
    '''
)
cursor.close()
print("Tabela Maquina criada com sucesso")