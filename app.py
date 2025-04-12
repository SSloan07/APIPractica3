from flask import Flask, jsonify, request, send_file, session
import random
from flask_session import Session
from ALGORITHM_1_LFCO_2025_AT_SS import StringGenerator
from ALGORITHM_2_LFCO_2025_AT_SS import PDA
from ALGORITHM_3_LFCO_2025_AT_SS import Rules_table

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Cambia esto por una clave secreta segura
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Crear instancias de las clases
stringGenerator = StringGenerator()
pda = PDA()
rules_table = Rules_table()  # Crear una instancia de Rules_table

@app.route('/')
def root():
    return send_file('index.html')

@app.route('/generate_strings', methods=['GET'])
def generate_strings():
    set_of_strings = stringGenerator.generateStrings()
    session['generated_strings'] = set_of_strings  # Almacenar los strings generados en la sesión
    emojis = ["🔥", "🌟", "💎", "📊", "👨‍💻", "💡", "⌨️", "🖱️", "🥑"]
    response = []
    for idx, s in enumerate(set_of_strings, 1):
        emoji = random.choice(emojis)
        response.append(f"{idx}. {s} {emoji}")
    return jsonify(response)

@app.route('/validate_strings', methods=['POST'])
def validate_strings():
    set_of_strings = session.get('generated_strings', [])  # Obtener los strings generados de la sesión
    results = []
    for string in set_of_strings:
        accepted, _ = pda.is_valid(string)
        checkmark = "✅" if accepted else "❌"
        results.append({'string': string, 'checkmark': checkmark})
        #print(f"String: {string}, Accepted: {accepted}, Checkmark: {checkmark}")
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)