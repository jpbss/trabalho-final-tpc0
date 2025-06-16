drop database if exists oficina;
create database if not exists oficina;

use oficina;

create table cliente(
	idcliente int primary key auto_increment,
	nome varchar(60),
    endereco varchar(80),
    cidade varchar(80),
    uf varchar(2),
    cep varchar(9)
);

create table veiculo(
	idplaca varchar(9) primary key,
    ano int,
    modelo int,
    preco_fipe decimal(10, 2),
    fabricante varchar(50),
    modelo_veiculo varchar(60),
    cor varchar(20),
    preco_venda decimal(10, 2),
    total_despesa decimal(10,2)
);

create table venda(
	idvenda int primary key auto_increment, 
    data DATE,
    valor_vendido decimal(10,2),
    forma_pagamento varchar(40),
    idcliente int,
    idplaca varchar(9),
    foreign key (idcliente) references cliente(idcliente),
	foreign key (idplaca) references veiculo(idplaca)
);

create table compra(
	idcompra int primary key auto_increment,
    data date,
    valor_pago decimal(10,2),
    forma_pagamento varchar(40),
    idplaca varchar(9),
    idcliente int,
    foreign key (idplaca) references veiculo(idplaca),
    foreign key (idcliente) references cliente(idcliente)
);

create table prestador(
	idprestador int primary key auto_increment,
	nome_empresa varchar(60),
    cidade varchar(80),
    uf varchar(2),
    cep varchar(9)
);

create table despesa(
	idplaca varchar(9),
    iddespesa int auto_increment,
    descricao varchar(80),
    valor decimal(10, 2),
    data_servico date,
    idprestador int,
    primary key (iddespesa, idplaca),
    foreign key (idplaca) references veiculo(idplaca),
    foreign key (idprestador) references prestador(idprestador)
)

