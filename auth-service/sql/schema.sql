CREATE DATABASE lerya;

\c lerya;

CREATE TABLE person(
  id SERIAL NOT NULL PRIMARY KEY,
  name VARCHAR(100),
  father_last_name VARCHAR(100),
  mother_last_name VARCHAR(100),
  phone VARCHAR(15),
  email VARCHAR(20),
  address VARCHAR(150),
  password VARCHAR(50)
);

CREATE TABLE professional(
  cedula VARCHAR(30),
  authorized BOOLEAN DEFAULT = 'FALSE'
) INHERITS(person);

CREATE TABLE patient(
  number_ss VARCHAR(100)
) INHERITS(person);

CREATE TABLE manager(
  authorized BOOLEAN DEFAULT = 'TRUE'
) INHERITS(person);

CREATE TABLE practicing(
  institute VARCHAR(100),
  case_file VARCHAR(50),
  authorized BOOLEAN DEFAULT = 'FALSE'
) INHERITS(person);

CREATE TABLE superuser(
  authorized BOOLEAN DEFAULT = 'TRUE'
) INHERITS(person);

CREATE TABLE permission(
  scope TEXT[][]
);
