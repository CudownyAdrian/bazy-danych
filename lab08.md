# Zadanie 1
```sql
create table kreatura as select * from wikingowie.kreatura;
create table uczestnicy as select * from wikingowie.uczestnicy;
create table etapy_wyprawy as select * from wikingowie.etapy_wyprawy;
create table sektor as select * from wikingowie.sektor;
create table wyprawa as select * from wikingowie.wyprawa;
```
```sql
 select nazwa,id_uczestnika from kreatura k  left join uczestnicy u on u.id_uczestnika=k.idKreatury where id_uczestnika is null;
```
```sql
select w.nazwa,sum(e.ilosc) from wyprawa w inner join uczestnicy u on w.id_wyprawy=u.id_wyprawy 
inner join ekwipunek e on u.id_uczestnika=e.idKreatury group by w.nazwa;
```

# Zadanie 2
```sql
select w.nazwa,count(distinct u.id_uczestnika),group_concat(k.nazwa separator ' | ') from wyprawa w 
inner join uczestnicy u on w.id_wyprawy=u.id_wyprawy 
inner join kreatura k on u.id_uczestnika=k.idKreatury
group by w.nazwa;
```
```sql
select w.nazwa,e.idEtapu,s.nazwa,k.nazwa from wyprawa w inner join kreatura k on w.kierownik=k.idKreatury
inner join etapy_wyprawy e on w.id_wyprawy=e.idWyprawy 
inner join sektor s on e.sektor=s.id_sektora
order by w.data_rozpoczecia,e.kolejnosc;
```

# Zadanie 3
```sql
select s.nazwa,count(e.sektor) from sektor s inner join etapy_wyprawy e on s.id_sektora=e.sektor group by s.nazwa
```
