# Services/Tabela_Professor.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
<<<<<<< HEAD
        CREATE TABLE Professor(
            CPF_Professor INTEGER (11) UNIQUE NOT NULL PRIMARY KEY,
            RG_Professor INTEGER (11) UNIQUE NOT NULL,
            Nome_Professor VARCHAR (255) NOT NULL,
            Horarios_Professor TIME NOT NULL,
            Telefone_Professor INTEGER (11) UNIQUE NOT NULL
        ) ENGINE=InnoDB;
=======
        CREATE TABLE IF NOT EXISTS Professor(
            CPF_Professor INTEGER NOT NULL PRIMARY KEY,
            RG_Prof INTEGER UNIQUE NOT NULL,
            Nome_Prof VARCHAR NOT NULL,
            Horarios_Prof TIME NOT NULL,
            Telefone_Prof INTEGER UNIQUE NOT NULL
        );
>>>>>>> 6f8c5ea (Terceiro Commit:)
    '''
)
cursor.close()
print("Tabela Professor criada com sucesso")