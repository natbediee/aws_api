from flask import Flask, jsonify 
import requests 
app = Flask(__name__) 
# URL de l'API FastAPI déployée sur l'instance EC2 
API_URL = "http://51.20.189.211/"
@app.route("/") 
def home(): 
    """Consomme l'endpoint / de l'API FastAPI.""" 
    try:
        response = requests.get(f"{API_URL}") 
        response.raise_for_status() 
        return jsonify({"message": "Données récupérées avec succès", "data": response.text}) 
    except requests.exceptions.RequestException as e: 
        return jsonify({"error": "Impossible de récupérer les données", "details": str(e)}), 500

@app.route("/get-test", methods=["GET"])

def get_test(): 
    """Consomme l'endpoint /test de l'API FastAPI.""" 
    try: 
        response = requests.get(f"{API_URL}test") 
        response.raise_for_status() 
        return jsonify({"message": "Données récupérées avec succès", "data": response.text}) 
    except requests.exceptions.RequestException as e: 
        return jsonify({"error": "Impossible de récupérer les données", "details": str(e)}), 500

if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0", port=5000)