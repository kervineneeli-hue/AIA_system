# TÄRKEÄÄ: Oikeassa toteutuksessa tämä vaatisi ulkoista sähköpostikirjastoa (esim. smtplib, SendGrid API)

def send_offer(problem_description, job_id):
    """Simuloi tarjouksen lähettämistä asiakkaalle."""
    
    # Lyhyt, tehokas tarjousviesti, joka ohjaa sivustolle (uskottavuus!)
    offer_message = (
        f"Hei, havaitsin ongelman {job_id} ({problem_description[:40]}...). "
        "AI-järjestelmämme on jo analysoinut tämän työn. "
        "Voimme toimittaa täydellisen ratkaisun tunnissa. "
        "Lataa tiedostosi turvallisesti osoitteessa [SIVUSTOSI_URL] ja saat hinnan heti."
    )
    # Tässä lähettäisit viestin oikeasti sähköpostilla tai alustan viestillä.
    return offer_message

def send_solution(job_id, client_email, solution_code):
    """Simuloi valmiin ratkaisun lähettämistä asiakkaalle maksun jälkeen."""
    
    final_message = (
        f"Kiitos tilauksesta {job_id}. Tässä on pyytämäsi valmis ratkaisu (Koodi/Data):"
        f"\n\n{solution_code}"
    )
    
    # Tässä lähettäisit final_message -viestin client_email -osoitteeseen
    # Esim. 'smtp_client.send_email(client_email, "Valmis Ratkaisusi", final_message)'
    
    print(f"Toimitus onnistui sähköpostiin {client_email}.")
    return "OK"

if __name__ == "__main__":
    test_offer = send_offer("Pieni bugi JS-koodissa", "TEST_ID_1")
    print(f"Testitarjous: {test_offer}")
    send_solution("TEST_ID_2", "testi@esim.com", "print('Hello World')")
