# Services/Tabela_Maquina.py

import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS Maquina(
            Nome_Maquina TEXT NOT NULL PRIMARY KEY,
            ID_Maquina INTEGER UNIQUE NOT NULL,
            Parte_Trabalhada TEXT NOT NULL
        );
    '''
)
cursor.close()
print("Tabela Maquina criada com sucesso")