# Zadania lab05
# Zadanie 1
```sql
delete from postac
where nazwa<>'Bjorn'
and rodzaj='wiking'
order by data_ur asc limit 2;
```
```sql
alter table walizka
drop foreign key walizka_ibfk_1;
alter table przetwory
drop foreign key przetwory_ibfk_1;
alter table przetwory
drop foreign key przetwory_ibfk_2;
alter table postac modify id_postaci int;
alter table postac drop primary key;
```
# Zadanie 2
```sql
alter table postac
add column pesel char(11) first;
update postac set pesel='64536748732'+id_postaci;
alter table postac add primary key(pesel);
```
```sql
alter table postac modify rodzaj enum('wiking','ptak','kobieta','syrena');
```
```sql
insert into postac values(('64536748740'),8,'Gertruda nieszczera','syrena','2000-09-09',60,null,null)
```

# Zadanie 3
```sql
update postac set statek='Wielka Fryta' where nazwa like '%a%';
```
```sql
update statek set max_ladownosc=max_ladownosc*0.7 where data_wodowania between '1901-01-01' and '2000-12-31';
```
```sql
alter table postac
add check(wiek<=1000)
```

# Zadanie 4
```sql
alter table postac modify rodzaj enum('wiking','ptak','kobieta','syrena','wąż');
insert into postac values('64536748741',9,'Loko','wąż','2000-09-11',5,null,null)
```
```sql
create table marynarz like postac;
insert into marynarz select * from postac where statek is not null;
```
```sql
alter table marynarz add foreign key(statek) references statek(nazwa_statku);
```

# Zadanie 5
```sql
update postac set statek=null;
```
```sql
delete from postac where rodzaj='wiking' and nazwa<>'Bjorn' limit 1;
```
```sql
alter table postac drop foreign key postac_ibfk_1;
alter table marynarz drop foreign key marynarz_ibfk_1;
delete from statek;
```
```sql
drop table statek;
```
```sql
create table zwierz(
id int primary key auto_increment,
nazwa varchar(50),
wiek int);
```
```sql
insert into zwierz(nazwa,wiek) select nazwa,wiek from postac where rodzaj='ptak' or rodzaj='wąż';
```
