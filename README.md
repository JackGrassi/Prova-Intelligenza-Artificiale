# Prova-Intelligenza-Artificiale


Setup del Progetto
Segui questi passaggi per configurare ed eseguire il progetto sul tuo sistema locale.

Prerequisiti
Prima di iniziare, assicurati di avere installato quanto segue:

Python 3.8+: Puoi scaricarlo da python.org.
pip: Il gestore di pacchetti di Python, solitamente incluso con Python.
Installazione
Clona il repository (o crea i file):
Se non hai un repository Git, crea una nuova cartella per il tuo progetto e al suo interno crea i file app.py, index.html e la cartella static con style.css.

Bash

# Se stai clonando un repository
git clone <URL_DEL_TUO_REPOSITORY>
cd <nome_cartella_progetto>
Crea un ambiente virtuale (consigliato):
È buona pratica creare un ambiente virtuale per isolare le dipendenze del tuo progetto.

Bash

python -m venv venv
Attiva l'ambiente virtuale:

macOS / Linux:
Bash

source venv/bin/activate
Windows:
Bash

venv\Scripts\activate
Installa le dipendenze:

Bash

pip install Flask google-generativeai python-dotenv
Configurazione della Chiave API di Google Gemini
Per utilizzare l'API di Google Gemini, avrai bisogno di una chiave API.

Ottieni la tua chiave API:

Visita la Google AI Studio o la console Google Cloud.
Crea un nuovo progetto o seleziona uno esistente.
Genera una nuova chiave API.
Crea un file .env:
Nella directory principale del tuo progetto (dove si trova app.py), crea un file chiamato .env e aggiungi la tua chiave API in questo formato:

GEMINI_API_KEY="LA_TUA_CHIAVE_API_QUI"
Sostituisci "LA_TUA_CHIAVE_API_QUI" con la chiave API che hai ottenuto.

Importante: Non condividere mai il tuo file .env o la tua chiave API pubblicamente (ad esempio, su GitHub)!

Guida all'uso
Dopo aver completato il setup del progetto, puoi iniziare a usare Cocktail AI:

Avvia l'applicazione Flask:
Assicurati che il tuo ambiente virtuale sia attivo, quindi esegui:

Bash

python app.py
Dovresti vedere un output simile a questo, che indica l'indirizzo a cui è in esecuzione l'applicazione:

 * Serving Flask app 'app'
 * Debug mode: on
INFO:werkzeug: * Running on http://127.0.0.1:5000
Press CTRL+C to quit
Apri il browser:
Apri il tuo browser web preferito e vai all'indirizzo fornito (solitamente http://127.0.0.1:5000/).

Inserisci gli ingredienti:
Nella casella di testo, digita gli ingredienti che hai a disposizione, separati da virgole (es. vodka, lime, menta).

Chiedi un cocktail:
Clicca sul pulsante "Chiedi". L'applicazione invierà la tua richiesta all'API di Google Gemini.

Visualizza la ricetta:
Dopo un breve caricamento, vedrai una o più ricette di cocktail che puoi preparare con gli ingredienti forniti. Ogni ricetta includerà il nome del cocktail, gli ingredienti con le quantità e i passaggi per la preparazione.

Gestione degli errori:
Se si verifica un problema (ad esempio, un formato di risposta inatteso dall'API o un errore di connessione), un messaggio di errore verrà visualizzato nell'area dei risultati, aiutandoti a diagnosticare il problema.
