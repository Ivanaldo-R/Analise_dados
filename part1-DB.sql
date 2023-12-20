CREATE TABLE Cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50),
    idade INTEGER,
    valor_fatura DECIMAL,
    pagamento BOOL
);

INSERT INTO Cliente (nome, idade, valor_fatura, pagamento) VALUES ("Sherlon", 28, 2599.99, True);