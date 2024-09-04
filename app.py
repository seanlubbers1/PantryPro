from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Set up your OpenAI API key
openai.api_key = "<REPLACE_WITH_API_KEY>"  # Replace with your actual API key

def generate_response(user_input):
    try:
        modified_input = "Based on—but not limited to—the following ingredients, give me a recipe that I can create. Use emojis in the response, and limit the output to 150 tokens: " + user_input
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": modified_input}
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return no content, 204 status

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    
    if user_input:
        ai_response = generate_response(user_input)
        return jsonify({"response": ai_response})
    else:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
