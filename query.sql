DROP DATABASE IF EXISTS remotedb;
CREATE DATABASE IF NOT EXISTS remotedb CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

DROP TABLE IF EXISTS Adds;
DROP TABLE IF EXISTS Keysession_table;
DROP TABLE IF EXISTS Session_table;
DROP TABLE IF EXISTS Appliance_consumption;
DROP TABLE IF EXISTS Appliance;
DROP TABLE IF EXISTS Rates;
DROP TABLE IF EXISTS Bi_Hour_Rate;
DROP TABLE IF EXISTS Flat_Rate;
DROP TABLE IF EXISTS Contract;
DROP TABLE IF EXISTS Employee;
DROP TABLE IF EXISTS Client;
DROP TABLE IF EXISTS Role;

CREATE TABLE Role (
    id int NOT NULL AUTO_INCREMENT,
    tipo varchar(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Client (
    id int NOT NULL AUTO_INCREMENT,
    username varchar(255) NOT NULL,
    nome varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    morada varchar(550),
    nif varchar(550),
    iban varchar(550),
    email  varchar(550),
    telefone  varchar(550),
    PRIMARY KEY (id)
);

CREATE TABLE Employee (
    id int NOT NULL AUTO_INCREMENT,
    username varchar(255) NOT NULL,
    nome varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    roleID int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (roleID) REFERENCES Role(id)
);

CREATE TABLE Contract (
    id int NOT NULL AUTO_INCREMENT,
    tipo varchar(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Flat_Rate (
    id int NOT NULL AUTO_INCREMENT,
    rate DOUBLE NOT NULL,
    contractID int NOT NULL,
    FOREIGN KEY (contractID) REFERENCES Contract(id),
    PRIMARY KEY (id)
);

CREATE TABLE Bi_Hour_Rate (
    id int NOT NULL AUTO_INCREMENT,
    rate1 DOUBLE NOT NULL, 
    rate2 DOUBLE NOT NULL, 
    initial TIMESTAMP, 
    finish TIMESTAMP,
    contractID int NOT NULL,
    FOREIGN KEY (contractID) REFERENCES Contract(id),
    PRIMARY KEY (id)
);

CREATE TABLE Appliance (
    id int NOT NULL AUTO_INCREMENT,
    nome varchar(255) NOT NULL,
    maxConsumption DOUBLE NOT NULL,
    isProducing BOOLEAN NOT NULL,
    contractID int NOT NULL,
    clientID int NOT NULL,
    FOREIGN KEY (clientID) REFERENCES Client(id),
    FOREIGN KEY (contractID) REFERENCES Contract(id),
    PRIMARY KEY (id)
);

CREATE TABLE Appliance_consumption (
    id int NOT NULL AUTO_INCREMENT,
    applianceID int NOT NULL,
    ts TIMESTAMP NOT NULL,
    consumption DOUBLE NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (applianceID) REFERENCES Appliance(id)
);

CREATE TABLE Session_table (
    id int NOT NULL AUTO_INCREMENT,
    clientID int NOT NULL,
    ts TIMESTAMP NOT NULL,
    rnd_hash VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (clientID) REFERENCES Client(id)
);

CREATE TABLE Keysession_table (
    keysession VARCHAR(500) NOT NULL,
    rnd_hash VARCHAR(256) NOT NULL,
    ts TIMESTAMP NOT NULL,
    PRIMARY KEY (keysession)
);
CREATE TABLE Adds (
    id int NOT NULL AUTO_INCREMENT,
    content VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
