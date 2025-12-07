from openai import OpenAI
import os

# MUISTA: KORVAA TÄMÄ OMALLA API-AVAIMELLASI!
# Oikeassa toteutuksessa käyttäisit mieluummin ympäristömuuttujaa
# Esim. client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
API_KEY = "[SINUN_OPENAI_TAI_GEMINI_API_AVAIN_TÄHÄN]" 

client = OpenAI(api_key=API_KEY) 

def process_problem(problem_description):
    """Käyttää AI:ta luomaan ratkaisun annettuun ongelmaan."""
    
    # Optimoidut ohjeet tekoälylle (The Prompt)
    system_prompt = (
        "Olet erittäin tehokas ja tiivis tekninen ratkaisija. Vastaa suoraan koodilla tai "
        "tarkalla ohjeella, joka ratkaisee ongelman. Älä selitä itseäsi. Sisällytä vain ratkaisu."
    )
    
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # Nopeampi, kustannustehokkaampi malli
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Ratkaise seuraava tekninen ongelma: {problem_description}"}
            ]
        )
        
        # Palauta vain tekoälyn luoma sisältö
        solution = completion.choices[0].message.content
        return solution
        
    except Exception as e:
        return f"VIRHE: Tekoälyratkaisun luominen epäonnistui: {e}"

if __name__ == "__main__":
    test_problem = "Luo Python-funktio, joka laskee Fibonaccin sarjan 10. luvun."
    solution = process_problem(test_problem)
    print("--- TESTIRATKAISU ---")
    print(solution)
