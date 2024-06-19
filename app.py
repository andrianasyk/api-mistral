from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Route principale de l'API REST
@app.route('/api/mistral', methods=['GET'])
def get_mistral_data():
    # Obtenir la requête passée en paramètre GET
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Missing 'q' parameter"}), 400

    # Construire l'URL de l'API distante avec le paramètre de requête
    url = f"https://hashier-api-groq.vercel.app/api/groq/mistral?ask={query}"

    # Faire une requête HTTP GET à l'API distante
    response = requests.get(url)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to retrieve data from the remote API"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
