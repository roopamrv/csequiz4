Drop table if exists datas;

-- CREATE TABLE datas(
--    namee varchar(6)  NOT NULL  
--   ,abb varchar(2)  NOT NULL
--   ,yearr INTEGER  NOT NULL
--   ,cost Integer not null

CREATE TABLE datas(
   name VARCHAR(10)  NOT NULL PRIMARY KEY 
  ,abb VARCHAR(10)  NOT NULL
  ,year INTEGER  NOT NULL
  ,cost INTEGER NOT NULL

);

INSERT INTO datas(name ,abb, year, cost) VALUES ('allen', 'al', 1998,40);
INSERT INTO datas(name ,abb, year, cost) VALUES ('betty', 'bt', 2010, 20);
INSERT INTO datas(name ,abb, year, cost) VALUES ('cat','ct', 2012, 10);
INSERT INTO datas(name,abb, year, cost) VALUES ('doll','dl',2000,30);
-- INSERT INTO datas(name,abb,year, cost) VALUES (5,300,16);
-- INSERT INTO datas(name,abb,year, cost) VALUES (6,27,18);
-- INSERT INTO datas(name,abb,year, cost) VALUES (7,28,29);
-- INSERT INTO datas(name,abb,year, cost) VALUES (8,144,45);
-- INSERT INTO datas(name,abb,year, cost) VALUES (9,222,38);
-- INSERT INTO datas(name,abb,year, cost) VALUES (10,223,20);
-- INSERT INTO datas(name,abb,year, cost) VALUES (11,72,29);
-- INSERT INTO datas(name,abb,year, cost) VALUES (12,219,10);
-- INSERT INTO datas(name,abb,year, cost) VALUES (13,89,6);
