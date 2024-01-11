# Zad1
```sql
select imie,nazwisko,data_urodzenia from pracownik;
```
# Zad2
```sql
select imie,nazwisko,Year(now())-year(data_urodzenia) as wiek from pracownik;
```
# Zad3
```sql
select d.nazwa,count(p.id_pracownika) from dzial d inner join pracownik p on d.id_dzialu=p.dzial group by d.nazwa;
```
# Zad4
```sql
select k.nazwa_kategori,count(t.id_towaru) from kategoria k inner join towar t on k.id_kategori=t.kategoria group by k.nazwa_kategori;
```
# Zad5
```sql
select k.nazwa_kategori,group_concat(t.nazwa_towaru) from kategoria k inner join towar t on k.id_kategori=t.kategoria group by k.nazwa_kategori;
```
# Zad6
```sql
select Round(avg(pensja),2) from pracownik;
```
# Zad7
```sql
select Round(avg(pensja),2) from pracownik where (year(now())-year(data_zatrudnienia))>5 ;
```
# Zad8
```sql
select nazwa_towaru,count(towar) from pozycja_zamowienia p inner join towar t on p.towar=t.id_towaru group by nazwa_towaru order by count(towar) desc limit 10;
```
# Zad9
```sql
select numer_zamowienia,sum(ilosc*cena) from zamowienie z inner join pozycja_zamowienia p on z.id_zamowienia=p.zamowienie where data_zamowienia between '2017-01-01'and '2017-03-31' group by id_zamowienia;
```
# Zad10
```sql
select imie,nazwisko,sum(ilosc*cena) from pracownik p inner join zamowienie z on p.id_pracownika=z.pracownik_id_pracownika inner join pozycja_zamowienia pz on z.id_zamowienia=pz.zamowienie group by id_pracownika order by sum(ilosc*cena) desc;
```

# Część 2
# Zad1
```sql

```
