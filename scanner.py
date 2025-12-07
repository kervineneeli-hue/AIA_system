import requests
from bs4 import BeautifulSoup

# Simuloitu lista tekoälypalveluista, joita skanneri etsii
KEYWORDS = ["Python automation", "data cleaning script", "SEO metadata fix", "Small JS bug"]

def run_scanner():
    """Simuloi verkon skannausta löytääkseen potentiaalisia töitä."""
    
    # KÄYTÄNNÖN TOTEUTUS: Tässä korvaisit tämän simulaation oikealla koodilla, joka kaapii tietoja
    # oikeilta sivustoilta (esim. freelancer-foorumeilta tai hakukoneista).
    
    # Esimerkki skannatusta datasta (Simuloi 5 uutta korkean arvon työtä)
    simulated_jobs = [
        {'id': 'HIGH_VALUE_101', 'description': 'Tarvitsen Python-skriptin 400 CSV-tiedoston yhdistämiseen ja normalisointiin.', 'price': 500, 'client_email': 'asiakas1@esim.com'},
        {'id': 'LOW_VALUE_202', 'description': 'Pieni bugi verkkosivun ostoskorin JavaScriptissä.', 'price': 150, 'client_email': 'asiakas2@esim.com'},
        {'id': 'HIGH_VALUE_103', 'description': 'Analysoi 5000 rivin datajoutkko ja luo lyhyt yhteenveto tekoälyä käyttäen.', 'price': 700, 'client_email': 'asiakas3@esim.com'},
        {'id': 'LOW_VALUE_204', 'description': 'Päivitä 50 tuotesivun SEO-metatiedot avainsanalla X.', 'price': 250, 'client_email': 'asiakas4@esim.com'},
        {'id': 'HIGH_VALUE_105', 'description': 'Luo pieni REST API-rajapinta, joka noutaa säätiedot.', 'price': 800, 'client_email': 'asiakas5@esim.com'},
    ]
    
    return simulated_jobs

if __name__ == "__main__":
    print("Scanner-testi: ")
    jobs = run_scanner()
    for job in jobs:
        print(f"- {job['id']}: {job['description'][:30]}...")
