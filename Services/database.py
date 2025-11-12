# Services/database.py 
import sqlite3 
 
server = ''
username = ''
password = ''
database = 'Academia.db'
conexao = sqlite3.connect("Academia.db")
print("Banco de dados da Academia foi criado com sucesso. ")
 