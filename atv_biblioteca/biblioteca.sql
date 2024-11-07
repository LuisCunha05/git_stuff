-- Active: 1730375618989@@10.28.2.34@3306@biblioteca

use biblioteca;

create table usuario (
    id_usuario int PRIMARY key AUTO_INCREMENT,
    nome VARCHAR(50),
    cpf VARCHAR(30) UNIQUE,
    telefone VARCHAR(30)
);

create table livro (
    id_livro int primary key AUTO_INCREMENT,
    titulo VARCHAR(50),
    autor VARCHAR(50),
    genero VARCHAR(50),
    status_livro TINYINT, -- 1:disponivel,2-emprestado,3-extraviado,4-danificado
    isbn VARCHAR(50) UNIQUE
);

CREATE Table emprestimo (
    id_emprestimo int PRIMARY KEY AUTO_INCREMENT,
    id_livro int,
    id_usuario int,
    devolvido BOOLEAN,
    Foreign Key (id_livro) REFERENCES livro(id_livro),
    Foreign Key (id_usuario) REFERENCES usuario(id_usuario)
);

INSERT INTO livro (titulo, autor, genero, status_livro, isbn) VALUES
('O Alquimista', 'Paulo Coelho', 'Ficção', 1, '001'),
('1984', 'George Orwell', 'Distopia', 1, '002'),
('Dom Casmurro', 'Machado de Assis', 'Clássico', 1, '003'),
('A Revolução dos Bichos', 'George Orwell', 'Fábula', 1, '004'),
('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 'Infantil', 1, '005');

INSERT INTO usuario (nome, cpf, telefone) VALUES
('Maria Silva', '123.456.789-00', '(11) 98765-4321'),
('João Santos', '987.654.321-00', '(21) 99876-5432'),
('Ana Oliveira', '111.222.333-44', '(31) 91234-5678'),
('Carlos Pereira', '555.666.777-88', '(41) 93456-7890'),
('Fernanda Costa', '222.333.444-99', '(51) 94567-8901');
