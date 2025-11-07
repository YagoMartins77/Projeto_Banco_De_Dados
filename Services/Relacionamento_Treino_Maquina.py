# Services/Relacionamento_Treino_Maquina.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE Treino_Maquina(
            ID_Treino INTEGER (11) UNIQUE NOT NULL,
            Nome_Maquina VARCHAR (255) UNIQUE NOT NULL,
            PRIMARY KEY (ID_Treino, Nome_Maquina),
            FOREIGN KEY ID_Treino REFERENCES Treino(ID_Treino),
            FOREIGN KEY Nome_Maquina REFERENCES Maquina(Nome_Maquina))
        ) ENGINE=InnoDB;
    '''
)
cursor.close()
print("Tabela Treino_Maquina criada com sucesso")