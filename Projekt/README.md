# Python2020 - Projekt Baza Danych
## Co projekt powinien mieć
Baza danych książek, płyt, itp.  - **TAK**
Baza powinna być zapisywana do pliku (txt, CSV, JSON). - **TAK**
Operacje na bazie: wstawianie, usuwanie, wyszukiwanie, listowanie. - **TAK**

## Opis - co projekt ma
Baza przechowywana jest w pliku tekstowym json.  
Operacje na danych:
 - SELECT
 - INSERT
 - UPDATE
 - DELETE
Plik projekt.db zawiera dwie przykładowe tablice: movies oraz books
Obsługa SQL jest dość prymitywna bo:
 - brak sortowania rekordów
 - brak kluczy głównych
 - brak ochrony przed duplikacją rekordów
ale to nie było tematem projektu.

### Wywołanie
```
usage: main.py [-h] [file]

positional arguments:
  file        file with database [default=:memory:]

optional arguments:
  -h, --help  show this help message and exit
```
### Pomoc
```
  db> help
Program help:
  help - this message
  .exit - exits shell
  .open <file_path> - open database in file if file doesn't exists it'll creates file on save
  .save <file_path> - saves database to file and switches to it
  .file - shows current database file
  .schema - shows current database tables

SQL Help(case-sensitive):
  SELECT * | col[,cols...] FROM table [WHERE ...]
  INSERT INTO table[(cols...)] VALUES(vals...)
  DELETE FROM table [WHERE ...]
  UPDATE table SET col1=val1[,...] [WHERE ...]
  CREATE TABLE table(col1,[cols...])
  DROP TABLE table
  COMMIT
  ROLLBACK

WHERE conditions examples:
  id=1 AND name LIKE '<regex>'
  id=2 OR (name LIKE '<regex>' AND year<2000)
```

## Przykłady
Baza otwarta za pomocą:
```
python main.py projekt.db
```
```
db> INSERT INTO movies('The Godfather',1972)
SQLException:  Invalid Syntax near INTO
db> INSERT INTO movies VALUES('The Godfather',1972)
Rows affected: 1
db> INSERT INTO movies VALUES('The Godfather II',1974)
Rows affected: 1
db> COMMIT
Database saved.
db> SELECT year,name FROM movies  
year|name                         
2013|Attack On Titan              
1972|The Godfather                
1974|The Godfather II             
db> SELECT niemamnie FROM movies
SQLException:  column niemamnie doesn't exists
db> UPDATE movies SET name='Zmiana' WHERE year=2013
Rows affected: 1
db> SELECT year,name FROM movies
year|name
2013|Zmiana
1972|The Godfather
1974|The Godfather II
db> ROLLBACK
Database restored.
db> SELECT year,name FROM movies
year|name
2013|Attack On Titan
1972|The Godfather
1974|The Godfather II

db> .open testdb.json
Database testdb.json loaded.
db> SELECT * FROM tabela1
id|name|year
1|Najgorszy Rok|2020
2|Niewiadomy Rok|2023
3|TEST|2000
-1|Puste|None
db> SELECT * FROM tabela1 WHERE year<20
SQLException:  '<' not supported between instances of 'NoneType' and 'int'

db> .open :memory:
Database :memory: loaded.
db> COMMIT
SQLException:  Can't commit :memory: database. Use SAVE before
db> CREATE TABLE test(id,name,surname,salary)
db> .schema
Tables in database[:memory:]:
test(id,name,surname,salary)
db>
```

