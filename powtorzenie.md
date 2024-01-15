## Zad1
```sql
select imie,nazwisko,data_urodzenia from pracownik;
```
## Zad2
```sql
select imie,nazwisko,Year(now())-year(data_urodzenia) as wiek from pracownik;
```
## Zad3
```sql
select d.nazwa,count(p.id_pracownika) from dzial d inner join pracownik p on d.id_dzialu=p.dzial group by d.nazwa;
```
## Zad4
```sql
select k.nazwa_kategori,count(t.id_towaru) from kategoria k inner join towar t on k.id_kategori=t.kategoria group by k.nazwa_kategori;
```
## Zad5
```sql
select k.nazwa_kategori,group_concat(t.nazwa_towaru) from kategoria k inner join towar t on k.id_kategori=t.kategoria group by k.nazwa_kategori;
```
## Zad6
```sql
select Round(avg(pensja),2) from pracownik;
```
## Zad7
```sql
select Round(avg(pensja),2) from pracownik where (year(now())-year(data_zatrudnienia))>5 ;
```
## Zad8
```sql
select nazwa_towaru,count(towar) from pozycja_zamowienia p inner join towar t on p.towar=t.id_towaru group by nazwa_towaru order by count(towar) desc limit 10;
```
## Zad9
```sql
select numer_zamowienia,sum(ilosc*cena) from zamowienie z inner join pozycja_zamowienia p on z.id_zamowienia=p.zamowienie where data_zamowienia between '2017-01-01'and '2017-03-31' group by id_zamowienia;
```
## Zad10
```sql
select imie,nazwisko,sum(ilosc*cena) from pracownik p inner join zamowienie z on p.id_pracownika=z.pracownik_id_pracownika inner join pozycja_zamowienia pz on z.id_zamowienia=pz.zamowienie group by id_pracownika order by sum(ilosc*cena) desc;
```

# Część 2
## Zad1
```sql
select nazwa,min(pensja),max(pensja),avg(pensja) from dzial d inner join pracownik p on d.id_dzialu=p.dzial group by nazwa;
```
## Zad2
```sql
select pelna_nazwa,sum(ilosc*cena) from klient k inner join zamowienie z on k.id_klienta=z.klient inner join pozycja_zamowienia p on z.id_zamowienia=p.zamowienie group by id_zamowienia order by sum(ilosc*cena) desc limit 10
```
## Zad3
```sql
select year(data_zamowienia),sum(cena * ilosc) as suma from zamowienie z inner join pozycja_zamowienia p on z.id_zamowienia=p.zamowienie group by year(data_zamowienia) order by suma desc;
```
## Zad4
```sql
select sum(cena*ilosc) from zamowienie z inner join pozycja_zamowienia p on z.id_zamowienia=p.zamowienie where status_zamowienia=6;
```
## Zad5
```sql
select miejscowosc,count(id_zamowienia),sum(cena*ilosc) from zamowienie z inner join pozycja_zamowienia p on z.id_zamowienia=p.zamowienie inner join adres_klienta a on z.klient=a.klient where typ_adresu=1 group by miejscowosc;
```
## Zad6
```sql
select sum(cena*ilosc) from pozycja_zamowienia p inner join zamowienie z on p.zamowienie=z.id_zamowienia where not status_zamowienia=6;
```
## Zad7
```sql
select Year(data_zamowienia),sum(cena*ilosc)-sum(cena_zakupu*ilosc) from pozycja_zamowienia p inner join zamowienie z on p.zamowienie=z.id_zamowienia inner join towar t on p.towar=t.id_towaru group by year(data_zamowienia);
```
## Zad8
```sql
select nazwa_kategori,sum(cena*sm.ilosc) from stan_magazynowy sm inner join pozycja_zamowienia p on sm.towar=p.towar inner join towar t on sm.towar=t.id_towaru inner join kategoria k on t.kategoria=k.id_kategori group by nazwa_kategori;
```
## Zad9
```sql
select monthname(data_urodzenia) as miesiac,count(id_pracownika) as 'liczba pracownikow' from pracownik group by miesiac order by FIELD(miesiac,'January', 'February', 'March', 'April', 'May', 'June', 
'July','August','September','October','November','December');
```
## Zad10
```sql

```
