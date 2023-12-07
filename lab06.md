# Zadanie 1
```sql
create table infs_mindaka.kreatura as select * from kreatura;
create table infs_mindaka.zasob as select * from zasob;
create table infs_mindaka.ekwipunek as select * from ekwipunek;
```
```sql
select * from zasob;
```
```sql
select * from zasob where rodzaj='jedzenie';
```
```sql
select idZasobu,ilosc from ekwipunek where idkreatury in (1,3,5)
```

# Zadanie 2
```sql
select * from kreatura where udzwig>=50 and not rodzaj='wiedzma' or rodzaj is null and udzwig>=50; 
```
```sql
select * from zasob where waga between 2 and 5;
```
```sql
select * from kreatura where nazwa like '%or%' and udzwig between 30 and 70;
```

# Zadanie 3
```sql
select * from zasob where month(dataPozyskania)=7 or month(datapozyskania)=8;
```
```sql
select * from zasob where rodzaj is not null order by waga;
```
```sql
select * from kreatura where dataur is not null order by dataur limit 5;
```

# Zadanie 4
```sql
select distinct rodzaj from zasob;

select rodzaj from zasob group by rodzaj;
```
```sql
select concat(nazwa,'-',rodzaj) from kreatura where rodzaj like 'wi%';
```
```sql
select waga*ilosc as waga from zasob where year(datapozyskania) between 2000 and 20007 ;
```

# Zadanie 5
```sql
select nazwa,waga*0.7 as netto,waga*0.3 as odpadki from zasob where rodzaj='jedzenie';
```
```sql
select * from zasob where rodzaj is null;
```
```sql
select distinct rodzaj from zasob where nazwa like 'Ba%' or '%os' order by rodzaj;
```
