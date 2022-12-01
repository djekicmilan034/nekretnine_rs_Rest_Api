Projekat je zamisljen kao primena Web Scraper-a nad stranicom nekretnine.rs,
skladistenje podataka sa stranice u bazu podataka i izrada Rest Api-ja nad podacima.

Pre pokretanja skripti, potrebno je instalirati biblioteke koje se nalaze u requirements.txt.
Nakon toga potrebno je kreirati bazu podataka u pgAdmin-u(Postgresql) pod nazivom 'demo'.

Pokretanjem skripte baza.py, proveravamo da li postoji konekcija sa bazom 'demo', kao i tabela ukoliko ne postoji, 
skripta ce kreirati tabelu.
Nakon sto inicijalizujemo konekciju sa bazom, pokrecemo Web Scraper stranice
pokretanjem skripte main.py i time vrsimo skladistenje podata u bazu sa stranice nekretnine.rs
Rest Api se pokrece pokretanjem skripte api.py gde mozemo videti implementaciju:
Prikaz svih elemenata u bazi
Prikaz elementa po zadatim Id-jem
Pretraga po zadatim vrednostima
Dodavanje novih nekretnina u bazu
Izmenu postojecih nekretnina u bazi.