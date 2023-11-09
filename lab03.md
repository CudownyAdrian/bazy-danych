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
id_walizka int not null auto_increment Primary key,
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
