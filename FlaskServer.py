# app.py
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'Ysk-proj-5Xn1sEq151UZDuWrj6hIF6UoOHw2NPoKsPDk9ahiN0Ga-tmnoD3mXxtfpfM7kQoG1Njh8NhdwcT3BlbkFJvXc9O-dbEEO5sJ7kaOsehk-9uGY7izaT4e9ceFWKRvApptY93x8vKP2_7zwCOlMxPSWx9KuxMA'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received data:", data)

    # Send to ChatGPT (OpenAI API)
    prompt = f"Analyze this MT5 data: {data}. Recommend trading actions."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    reply = response['choices'][0]['message']['content']
    print("ChatGPT Response:", reply)

    return jsonify({"status": "success", "reply": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
