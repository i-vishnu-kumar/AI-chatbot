import os
from dotenv import load_dotenv
import google.generativeai as genai


class GeminiAPIBot:
    def __init__(self, api_key):
        self.gemini_api_key = api_key

        if not self.gemini_api_key:
            raise ValueError("API key is not provided...sorry!")
        
        genai.configure(api_key=self.gemini_api_key)

        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 100,
            "response_mime_type": "text/plain",
        }

        instruction = "You are a helpful chatbot"

        self.gemini = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            generation_config=generation_config,
            system_instruction=instruction
        )

        self.chat_session_gemini = self.gemini.start_chat(history=[])

    def get_gemini_response(self, prompt):
        try:
            response = self.chat_session_gemini.send_message(prompt)
            return response.text
        except Exception as e:
            return f"Oops! It seems I didn't get your question. Error: {e}"
        
if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    my_bot = GeminiAPIBot(api_key=api_key)
    its_response = my_bot.get_gemini_response("Who is president of Japan")
    print(its_response)
