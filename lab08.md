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
select s.nazwa,ifnull(count(e.sektor),0) as ilosc_odwiedzin  from sektor s left join etapy_wyprawy e on s.id_sektora=e.sektor group by s.nazwa;
```
```sql
select k.nazwa,if(count(id_uczestnika)>0,'bral udzial w wyprawie','nie bral udzialu w wyprawie') from kreatura k left join uczestnicy u on k.idKreatury=u.id_uczestnika group by k.nazwa;
```

# Zadanie 4
```sql
select w.nazwa,sum(length(dziennik)) from wyprawa w inner join etapy_wyprawy e on w.id_wyprawy=e.idWyprawy group by w.nazwa having sum(length(dziennik))<400;
```
```sql
select u.id_wyprawy,sum(waga*z.ilosc)/count(distinct id_uczestnika) from uczestnicy u inner join ekwipunek e on u.id_uczestnika=e.idKreatury 
inner join wyprawa w on u.id_wyprawy=w.id_wyprawy 
inner join zasob z on e.idZasobu=z.idZasobu  group by w.id_wyprawy;
```

# Zadanie 5
```sql
select k.nazwa,datediff(w.data_rozpoczecia,k.dataur) from kreatura k inner join uczestnicy u on k.idKreatury=u.id_uczestnika inner join wyprawa w on u.id_wyprawy=w.id_wyprawy inner join etapy_wyprawy ew on w.id_wyprawy=ew.idWyprawy inner join sektor s on ew.sektor=s.id_sektora where s.nazwa='Chatka dziadka';
```
