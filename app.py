from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

AI_API_URL = "https://api.esempio.com/v1/chat"  # <-- Sostituisci con l’URL reale
API_KEY = "la_tua_api_key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    ingredients = data.get("ingredients", "")

    prompt = f"Quali cocktail si possono fare con questi ingredienti: {ingredients}?"

    response = requests.post(
        AI_API_URL,
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"prompt": prompt, "max_tokens": 100}
    )

    if response.status_code == 200:
        answer = response.json().get("response", "Nessuna risposta.")
    else:
        answer = "Errore nella richiesta all'intelligenza artificiale."

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
