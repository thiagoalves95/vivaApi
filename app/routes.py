import requests
from flask import request, jsonify, render_template
from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/assistant', methods=['GET', 'POST'])
def assistant():
    if request.method == 'GET':
        return jsonify({
            'message': 'Use o método POST para enviar uma mensagem.',
            'example': {
                'message': 'Desenvolvi um projeto que aumentou a eficiência da equipe em 20%.'
            }
        })

    if request.method == 'POST':
        try:
            data = request.get_json()  # Use request.get_json() para garantir que o JSON está sendo processado corretamente
            app.logger.info(f"Received data: {data}")
        except Exception as e:
            app.logger.error(f"Error parsing JSON: {e}")
            return jsonify({'error': 'Invalid JSON', 'message': str(e)}), 400

        if not data:
            app.logger.error("No data received")
            return jsonify({'error': 'Invalid JSON'}), 400

        message = data.get('message')
        
        if not message:
            app.logger.error("No message provided")
            return jsonify({'error': 'No message provided'}), 400

        # Ajustar o prompt
        prompt = f"Você é um especialista em criação de currículos. Reescreva o seguinte texto de forma clara, concisa e profissional, adequada para um currículo, sem introduções desnecessárias e sem colchetes: {message}"

        headers = {
            'Authorization': f"Bearer {app.config['GROQ_API_KEY']}",
            'Content-Type': 'application/json'
        }
        payload = {
            'model': 'llama-3.2-1b-preview',
            'messages': [{'role': 'user', 'content': prompt}]
        }

        response = requests.post(app.config['GROQ_API_URL'], headers=headers, json=payload)
        
        if response.status_code != 200:
            app.logger.error(f"Failed to get response from Groq: {response.status_code}")
            return jsonify({'error': 'Failed to get response from Groq'}), response.status_code

        return jsonify(response.json())

# Adicione esta parte ao final do arquivo
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8002)