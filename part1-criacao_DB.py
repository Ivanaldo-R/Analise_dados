#Criacao DB estruturado para Análise de Clientes
import sqlite3
conexao = sqlite3.connect("database.sqlite3")
cursor = conexao.cursor()
##############################################

cursor.execute("""
CREATE TABLE Cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50),
    idade INTEGER,
    valor_fatura DECIMAL,
    pagamento BOOL
);""")

##############################################
conexao.commit()
cursor.close()