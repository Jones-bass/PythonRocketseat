CREATE TABLE IF NOT EXISTS 'pessoa_fisica' (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    idade INTEGER,
    email VARCHAR(100),
    telefone VARCHAR(20),
    cidade VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS 'pessoa_juridica' (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    razao_social VARCHAR(150) NOT NULL,
    nome_fantasia VARCHAR(150),
    cnpj VARCHAR(14) UNIQUE NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20),
    cidade VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO pessoa_fisica
(nome, cpf, idade, email, telefone, cidade)
VALUES
('Maria Silva', '12345678900', 25, 'maria@gmail.com', '79999999999', 'Aracaju'),

('João Santos', '98765432100', 31, 'joao@gmail.com', '79988888888', 'Lagarto'),

('Ana Oliveira', '11122233344', 28, 'ana@gmail.com', '79977777777', 'Tobias Barreto');


INSERT INTO pessoa_juridica
(razao_social, nome_fantasia, cnpj, email, telefone, cidade)
VALUES
('Mercado Bom Preco LTDA', 'Bom Preço', '12345678000199', 'contato@bompreco.com', '7933333333', 'Aracaju'),

('Tech Solutions LTDA', 'Tech Solutions', '99887766000155', 'suporte@tech.com', '7932222222', 'Lagarto'),

('Construtora Forte LTDA', 'Forte Engenharia', '44556677000188', 'engenharia@forte.com', '7931111111', 'Itabaiana');
