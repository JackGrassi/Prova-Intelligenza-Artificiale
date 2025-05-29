import os
import json
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    ingredients = data.get("ingredients", "")

    # Ho modificato il prompt per chiedere ESPLICITAMENTE un array di oggetti, se ci sono più opzioni.
    # Ho anche aggiunto un'istruzione per includere solo un cocktail se è l'unica opzione sensata.
    prompt = (
        f"Con questi ingredienti: {ingredients}, che cocktail posso preparare? "
        f"Rispondi in formato JSON con la seguente struttura, che può essere un singolo oggetto o un array di oggetti se ci sono più cocktail pertinenti. "
        f"Se c'è solo un cocktail rilevante, rispondi con un singolo oggetto JSON, altrimenti con un array:\n\n"
        f"""
        [
            {{
                "nome": "Nome del cocktail",
                "ingredienti": [
                    {{ "nome": "nome ingrediente", "quantità": "quantità" }}
                ],
                "ricetta": "Descrizione dei passaggi per prepararlo"
            }}
        ]
        """
        f"\n\nRispondi SOLO CON JSON, senza testo aggiuntivo. Assicurati che il JSON sia valido."
    )

    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(prompt)
        text = response.text

        # Tenta di parsare la risposta come JSON direttamente.
        # Questo è più robusto dell'estrazione manuale di graffe/parentesi.
        try:
            answer_data = json.loads(text)
        except json.JSONDecodeError as e:
            # Se il parsing fallisce, prova a fare un'estrazione più "intelligente"
            # cercando il primo '[' o '{' e l'ultimo ']' o '}'
            start_index = -1
            end_index = -1

            # Prova a trovare l'inizio di un array o di un oggetto
            first_brace_idx = text.find('{')
            first_bracket_idx = text.find('[')

            if first_bracket_idx != -1 and (first_brace_idx == -1 or first_bracket_idx < first_brace_idx):
                start_index = first_bracket_idx
                end_index = text.rfind(']')
            elif first_brace_idx != -1:
                start_index = first_brace_idx
                end_index = text.rfind('}')

            if start_index != -1 and end_index != -1:
                json_str = text[start_index : end_index + 1]
                try:
                    answer_data = json.loads(json_str)
                except json.JSONDecodeError as nested_e:
                    raise ValueError(f"Errore nel parsing JSON dopo estrazione: {nested_e}. Stringa JSON tentata: {json_str}")
            else:
                raise ValueError(f"Nessun blocco JSON valido (oggetto o array) trovato nella risposta dell'API. Errore originale: {e}")

        # Se il modello ha restituito un singolo oggetto, lo trasformiamo in un array di un elemento
        if isinstance(answer_data, dict):
            answer_data = [answer_data]

        # Assicurati che sia sempre una lista di dizionari
        if not isinstance(answer_data, list):
            raise ValueError(f"Formato JSON inatteso: la risposta non è un array o un oggetto valido. Tipo ricevuto: {type(answer_data)}")

        return jsonify(answer_data) # Restituisce direttamente l'array

    except Exception as e:
        return jsonify({
            "error": str(e),
            "raw_response": text if 'text' in locals() else "Nessuna risposta disponibile (errore prima della generazione)"
        })

if __name__ == '__main__':
    app.run(debug=True)