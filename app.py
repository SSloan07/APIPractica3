from flask import Flask, jsonify, send_file, session
import random
from flask_session import Session
from ALGORITHM_1_LFCO_2025_AT_SS import StringGenerator
from ALGORITHM_2_LFCO_2025_AT_SS import PDA
from ALGORITHM_3_LFCO_2025_AT_SS import Rules_table

app = Flask(__name__)
app.secret_key = 'supersecretkey' 
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Crear instancias de las clases
stringGenerator = StringGenerator()
pda = PDA()
rules_table = Rules_table() 

@app.route('/')
def root():
    return send_file('index.html')

@app.route('/generate_strings', methods=['GET'])
def generate_strings():
    set_of_strings = stringGenerator.generateStrings()
    session['generated_strings'] = set_of_strings  # Get the strings of the session
    emojis = ["🔥", "🌟", "💎", "📊", "👨‍💻", "💡", "⌨️", "🖱️", "🥑"]
    response = []
    for idx, s in enumerate(set_of_strings, 1):
        emoji = random.choice(emojis)
        response.append(f"{idx}. {s} {emoji}")
    return jsonify(response)

@app.route('/validate_strings', methods=['POST'])
def validate_strings():
    set_of_strings = session.get('generated_strings', [])  # Get the strings of the session
    results = []
    for string in set_of_strings:
        accepted, _ = pda.is_valid(string)
        checkmark = "✅" if accepted else "❌"
        results.append({'string': string, 'checkmark': checkmark})
    return jsonify(results)


# In this thrid algorithm we are going to show the rules applied to the strings that were accepted by the PDA, returning all the tables in html format.

@app.route('/validation_table', methods=['POST'])
def validation_table():
    set_of_strings = session.get('generated_strings', [])
    valid_strings = []
    transitions_done = []

    for string in set_of_strings:
        valid_stringsTemp, transitionTemp = pda.is_valid(string)
        if valid_stringsTemp:
            valid_strings.append(string)
            transitions_done.append(transitionTemp)

    all_tables_html = []

    for i in range(len(valid_strings)):
        string = valid_strings[i]
        transition_done = transitions_done[i]

        table_html = rules_table.aplied_rules(string, transition_done)
        all_tables_html.append(f"<h3>Tabla para cadena: <code>{string}</code></h3>{table_html}")

    # Combine all tables into a single HTML string
    full_html = "<br>".join(all_tables_html)
    return full_html


if __name__ == '__main__':
    app.run(debug=True)