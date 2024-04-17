from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with the API key you obtained from OpenAI
API_KEY = '' 
API_URL = 'https://api.openai.com/v1/images/generations'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_image', methods=['POST'])
def generate_image():
    prompt = request.json.get('prompt', '')
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': prompt,
        'n': 1,  # Number of images to generate
        'size': "1024x1024"  # Size of the generated image
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        image_url = response.json()['data'][0]['url']
        return jsonify({'image_url': image_url})
    else:
        return jsonify({'error': 'Failed to generate image', 'details': response.text}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
