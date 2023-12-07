# Zadanie 1
```sql
Select avg(waga) from kreatura where rodzaj='wiking';
```
```sql
Select avg(waga),count(idKreatury) from kreatura group by rodzaj;
```
```sql
Select avg(year(now())-year(dataur))from kreatura group by rodzaj;
```

# Zadanie 2
```sql
select sum(waga) from zasob group by rodzaj;
```
```sql
select avg(waga) from zasob group by nazwa having sum(ilosc)>=4 and sum(waga*ilosc)>10;
```
```sql
select count(distinct nazwa) as liczba from zasob group by rodzaj having min(liczba)>1;
```

# Zadanie 3
```sql
select k.nazwa,e.idZasobu,e.ilosc from kreatura k inner join ekwipunek e on k.idkreatury=e.idkreatury;
```
```sql
select k.nazwa,e.idZasobu,z.nazwa from kreatura k inner join ekwipunek e on k.idkreatury=e.idkreatury inner join zasob z on z.idZasobu=e.idzasobu;
```
```sql
select k.nazwa from kreatura k left join ekwipunek e on k.idKreatury=e.idKreatury where e.idkreatury is null;
```

# Zadanie 4
```sql
select k.nazwa, z.nazwa from kreatura k natural join ekwipunek e natural join zasob z where k.rodzaj='wiking' and year(dataur) between 1670 and 1679;
```
```sql
select k.nazwa from kreatura k inner join ekwipunek e on k.idkreatury=e.idkreatury inner join zasob z on e.idZasobu=z.idzasobu where z.rodzaj='jedzenie' order by year(now())-year(dataur) limit 5;
```
```sql
select concat(k1.nazwa,' - ',k2.nazwa) from kreatura k1 inner join kreatura k2 where k1.idkreatury-k2.idKreatury=5;
```


# Zadanie 5
```sql

```
