# Services/Tabela_Plano.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS Plano(
            Tipo_Plano TEXT NOT NULL PRIMARY KEY,
            ID_Plano INTEGER UNIQUE NOT NULL
        );
    '''
)
cursor.close()
print("Tabela Plano criada com sucesso")