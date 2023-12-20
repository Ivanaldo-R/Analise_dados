#Criação de um DB Sintético automaticamente
import sqlite3
from random import randint

conexao = sqlite3.connect("database.sqlite3")
cursor = conexao.cursor()
##############################################
def obtem_dados():
    #OBTENDO DADOS DO INPUT
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    valor_fatura = float(input("Digite o valor da fatura: "))
    pagamento = bool(int(input("Digite 1) Pago ou 0) Pendente: ")))

    comando_sql = """INSERT INTO Cliente (nome, idade, valor_fatura, pagamento) VALUES (?, ?, ?, ?);"""
    valores = [nome, idade, valor_fatura, pagamento]
    cursor.execute(comando_sql, valores)

def insere_dados(quantidade = 1):
    #GERANDO OS DADOS AUTOMATICAMENTE
    for i in range(quantidade):
        nomes = ["Sherlon", "Naldo", "Maria", "João", "Lucas"]
        sobrenomes = ["Lopes", "Almeida", "Cunha", "Costa", "Silva"]
        nome = nomes[randint(0, len(nomes)-1)] + " " + sobrenomes[randint(0, len(sobrenomes)-1)] 
        idade = randint(10, 100) #Valor entre [10, 100]
        valor_fatura = (randint(0, 1600000)/100)-1000 #Valor entre [-1000, 15000]
        
        pagamentos = [False, True, None]
        pagamento = pagamentos[randint(0, 2)]

        comando_sql = """INSERT INTO Cliente (nome, idade, valor_fatura, pagamento) VALUES (?, ?, ?, ?);"""
        valores = [nome, idade, valor_fatura, pagamento]
        cursor.execute(comando_sql, valores)

insere_dados(quantidade = 1000)

##############################################
conexao.commit()
cursor.close()