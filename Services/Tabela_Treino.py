# Services/Tabela_Treino.py 
 
import sqlite3
 
conexao = sqlite3.connect("Academia.db")
 
cursor = conexao.cursor()
 
cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS Treino(
            ID_Treino INTEGER NOT NULL PRIMARY KEY,
            Alongamentos TEXT,
            Exercicios_Aerobicos TEXT,
            Exercicios_Maquina TEXT,
            Carga INTEGER,
            CPF_Aluno INTEGER UNIQUE NOT NULL,
            FOREIGN KEY (CPF_Aluno) REFERENCES Aluno (CPF_Aluno)
        );
    '''
)
cursor.close()
print("Tabela Treino criada com sucesso")