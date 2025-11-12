# Services/Tabela_Personal.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
<<<<<<< HEAD
        CREATE TABLE Personal(
            CPF_Personal INTEGER (11) UNIQUE NOT NULL PRIMARY KEY,
            RG_Persona INTEGER (11) UNIQUE NOT NULL,
            Nome_Personal VARCHAR (255) NOT NULL,
            Horarios_Professor TIME NOT NULL,
            Telefone_Personal INTEGER (11) UNIQUE NOT NULL
        ) ENGINE=InnoDB;
=======
    CREATE TABLE IF NOT EXISTS Personal (
        CPF_Personal INTEGER PRIMARY KEY,
        RG_Personal INTEGER UNIQUE NOT NULL,
        Nome_Personal TEXT NOT NULL,
        Horarios_Personal TEXT NOT NULL,  -- formato "HH:MM:SS"
        Telefone_Personal INTEGER UNIQUE NOT NULL
    );
>>>>>>> 6f8c5ea (Terceiro Commit:)
    '''
)

cursor.close()
print("Tabela Personal criada com sucesso")