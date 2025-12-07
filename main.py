import time
from scanner import run_scanner
from resolver import process_problem
from closer import send_offer, send_solution

# Pääsilmukka asetukset
TARGET_INCOME = 5000 
CYCLE_DELAY_SECONDS = 60 * 30  # Tarkista 30 minuutin välein

def main_loop():
    """Ajaa AIA-systeemin automaattisen silmukan."""
    current_income = 0
    start_time = time.time()
    
    print(f"--- AIA-Systeemi käynnistetty. Tavoite: {TARGET_INCOME} euroa. ---")

    while current_income < TARGET_INCOME and (time.time() - start_time) < (72 * 3600):
        
        # 1. Skannaa uudet työpaikat
        print(f"\n[{time.strftime('%H:%M:%S')}] Ajan Scannerin...")
        new_jobs = run_scanner()
        
        if new_jobs:
            print(f"Löydettiin {len(new_jobs)} uutta työtä.")
            
            for job in new_jobs:
                job_id = job.get('id', 'N/A')
                problem_desc = job.get('description', 'Tuntematon ongelma')
                
                # 2. Luo tarjous (simuloitu)
                offer_text = send_offer(problem_desc, job_id)
                print(f"  -> Lähetetty tarjous työlle {job_id} ({offer_text[:50]}...)")
                
                # --- TÄSSÄ PAIKASSA KÄYTÄNNÖSSÄ ODOTETTAISIIN ASIAKKAAN HYVÄKSYNTÄÄ ---
                # Koska olemme nopeassa tilassa, simuloimme korkeaa hyväksyntäprosenttia.
                if job_id.startswith('HIGH_VALUE'): 
                    
                    # 3. Ratkaise ongelma heti hyväksynnän jälkeen
                    print(f"  -> Työ {job_id} hyväksytty! Kutsutaan Resolveria...")
                    solution_code = process_problem(problem_desc)
                    
                    # 4. Toimita ratkaisu ja kirjaa tulo
                    delivery_status = send_solution(job_id, job.get('client_email'), solution_code)
                    
                    if delivery_status == "OK":
                        job_price = job.get('price', 300) # Oletushinta 300
                        current_income += job_price
                        print(f"  -> Ratkaisu toimitettu. Ansaittu: {job_price} €. Kumulatiivinen tulo: {current_income} €.")
                        
        
        time.sleep(CYCLE_DELAY_SECONDS)

    print("\n--- Tavoite saavutettu tai 72 tuntia ummessa. ---")
    print(f"Lopullinen tulo: {current_income} €")

if __name__ == "__main__":
    main_loop()
