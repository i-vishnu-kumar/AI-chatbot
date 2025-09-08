from flask import Flask, render_template, jsonify, request
from ai_model.gemini import GeminiAPIBot
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__, template_folder="../frontend/template", static_folder="../frontend/static")

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/api/get_res_from_ai',methods=['POST'])
def getResponse():
    data = request.get_json()
    user_message = data['user_message']
    print(user_message)

    api_key = os.getenv("GOOGLE_API_KEY")
    my_bot = GeminiAPIBot(api_key=api_key)
    ai_response = my_bot.get_gemini_response(user_message)
    print(ai_response)

    return jsonify({'ai_response':ai_response})
