CREATE DATABASE lerya;

\c lerya;

CREATE TABLE person(
  id SERIAL NOT NULL PRIMARY KEY,
  name VARCHAR(100),
);

INSERT INTO person(name)
VALUES ('Lerya'),
       ('Jesus');
