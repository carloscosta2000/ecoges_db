DROP DATABASE IF EXISTS ecoges;
CREATE DATABASE IF NOT EXISTS ecoges CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

DROP TABLE IF EXISTS Appliance_consumption;
DROP TABLE IF EXISTS Appliance;
DROP TABLE IF EXISTS Rates;
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
    morada varchar(255) NOT NULL,
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

CREATE TABLE Rates (
    id int NOT NULL AUTO_INCREMENT,
    rate DOUBLE NOT NULL,
    initial TIMESTAMP,
    finish TIMESTAMP,
    contractID int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (contractID) REFERENCES Contract(id)
);

CREATE TABLE Appliance (
    id int NOT NULL AUTO_INCREMENT,
    nome varchar(255) NOT NULL,
    maxConsumption DOUBLE NOT NULL,
    isProducing BOOLEAN NOT NULL,
    contractID int NOT NULL,
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
    rnd_hash VARCHAR(64) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (clientID) REFERENCES Client(id)
);