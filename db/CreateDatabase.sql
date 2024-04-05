USE livraria;

CREATE TABLE livros (
    id integer not null auto_increment,
    titulo varchar(100),
    autor varchar(100),
    PRIMARY KEY(id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO livros ( titulo , autor) VALUES ( 'dioguinho', 'carlitos');
INSERT INTO livros ( titulo , autor) VALUES ('dioguinho 2', 'carlitos 2');
INSERT INTO livros ( titulo , autor) VALUES ( 'dioguinho 3', 'carlitos 3');