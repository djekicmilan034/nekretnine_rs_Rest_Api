Ideja projekta je implementacija Web Scraper-a nad stranicom nekretnine.rs i realizacija REST API sa podacima dobijenih pomocu Web Scraper-a.
U folderu template nalaze se html forme za dodavanje i azuriranje podataka. 
Pre pokretanja skripti potrebno je instalirati potrebne biblioteke koje se nalaze u requirements.txt
Potrebno je u pgAdminu(Postgresql) kreirati bazu 'demo'.

Na pocetku pokrecemo skrptu baza.py kako bi se povezali sa bazom i kreirali tabelu sa kolonama koje ce se popunjavati pokretanjem Web Scraper-a.
Da bi pokrenuli Web Scraper, pokrecemo skriptu main.py.
Dok se REST API nalazi i pokrece pokretanjem skripte api.py
