# Zadania lab03  
# Zadanie 1

```sql
Create table postac (
id_postaci int NOT NULL AUTO_INCREMENT Primary Key,
nazwa varchar(40),
rodzaj enum('wiking','ptak','kobieta'),
data_ur date,
wiek int unsigned
)
;
```
```sql
insert into postac values(default, 'Bjorn','wiking','2000-01-01',300);
insert into postac values(default, 'Drozd','Ptak','2010-01-01',10);
insert into postac values(default, 'Tesciowa','kobieta','1000-01-01',2000);
```
```sql
Update postac
set wiek=88
where id_postaci=3;
```

# Zadanie 2
```sql
Create table walizka(
id_walizka int not null AUTO_INCREMENT Primary key,
pojemnosc int unsigned,
kolor enum('różowy','czerwony','tęczowy','żółty'),
id_wlasciciela int,
Foreign key(id_wlasciciela) references postac(id_postaci) on delete cascade
)
;
```
```sql
alter table walizka alter column kolor set default 'różowy';
```
```sql
insert into walizka values(default,100,'tęczowy',1);
insert into walizka values(default,50,default,3);
```
# Zadanie 3
```sql
Create table izba(
adres_budynku varchar(50) not null,
nazwa_izby varchar(50) not null,
metraz mediumint unsigned,
wlasciciel int,
primary key(adres_budynku,nazwa_izby),
Foreign key(wlasciciel) references postac(id_postaci) on delete set null
)

```
```sql
alter table izba add column
kolor varchar(30) default'czarny'
after metraz;
```
```sql
insert into izba values('szkolna 17','spiżarnia',10,default,1)
```
# Zadanie 4
```sql
create table przetwory(
id_przetworu int not null primary key,
rok_produkcji smallint default 1654,
id_wykonawcy int ,
zawartosc varchar(50),
dodatek varchar(50) default'papryczka chili',
id_konsumenta int,
foreign key(id_wykonawcy) references postac(id_postaci),
foreign key(id_konsumenta) references postac(id_postaci)
)  
```
```sql
insert into przetwory values( default,default,3,'bigos',default,1)
```
# Zadanie 5
```sql
insert into postac values(default, 'Corn','wiking','2000-01-01',300),(default, 'Dis','wiking','2000-02-02',40),(default, 'Mietek','wiking','1999-03-03',777),(default, 'Marek','wiking','2000-07-07',47),(default, 'Franek','wiking','1989-05-04',66)
```
```sql
create table statek(
nazwa_statku varchar(50) not null primary key,
rodzaj_statku enum('drakar','galeon'),
data_wodowania date,
max_ladownosc smallint unsigned
)
```
```sql
insert into statek values('Fryta','drakar','2000-02-02',10),('Wielka Fryta','galeon','2010-10-10',100)
```
```sql
alter table postac
add column funkcja varchar(50)
```
```sql
update postac set funkcja='kapitan' where id_postaci=1
```
```sql
alter table postac add column statek varchar(50) 
alter table postac add foreign key(statek) references statek(nazwa_statku)
```
```sql
update postac set statek='Wielka Fryta' where rodzaj='wiking'
update postac set statek='Fryta' where rodzaj='ptak'
```
```sql
delete from izba where nazwa_izby='spiżarnia'
```
```sql
drop table izba
```
