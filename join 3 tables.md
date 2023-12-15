-- Cria a tabela `produto`
CREATE TABLE produto (
  id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  preco DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (id)
);

-- Insere dados na tabela `produto`
INSERT INTO produto (nome, preco) VALUES
  ('iPhone 14', 10000.00),
  ('Galaxy S23', 9000.00),
  ('MacBook Pro', 15000.00);

-- Cria a tabela `cupom`
CREATE TABLE cupom (
  id INT NOT NULL AUTO_INCREMENT,
  valor DECIMAL(10,2) NOT NULL,
  id_produto INT NOT NULL,
  id_cliente INT NOT NULL,
  data_venda DATETIME NOT NULL,
  PRIMARY KEY (id)
);

-- Insere dados na tabela `cupom`
INSERT INTO cupom (valor, id_produto, id_cliente, data_venda) VALUES
  (1000.00, 1, 1, '2023-07-20'),
  (500.00, 2, 2, '2023-08-03'),
  (2000.00, 3, 3, '2023-09-10');

-- Cria a tabela `cliente`
CREATE TABLE cliente (
  id INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  sexo CHAR(1) NOT NULL,
  PRIMARY KEY (id)
);

-- Insere dados na tabela `cliente`
INSERT INTO cliente (nome, email, sexo) VALUES
  ('João', 'joao@gmail.com', 'M'),
  ('Maria', 'maria@gmail.com', 'F'),
  ('José', 'jose@gmail.com', 'M');

-- Junta as três tabelas
SELECT
  produto.nome,
  cupom.valor,
  cliente.nome
FROM
  produto
JOIN
  cupom
  ON produto.id = cupom.id_produto
JOIN
  cliente
  ON cupom.id_cliente = cliente.id;
