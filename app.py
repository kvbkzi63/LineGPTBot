from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import openai
import os 
from flask_cors import CORS

app = Flask(__name__) 
CORS(app, resources={r"/*": {"origins": "*"}})


# LINE API tokens
LINE_CHANNEL_ACCESS_TOKEN = 'your_access_token'
LINE_CHANNEL_SECRET = 'your_secret'

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# OpenAI API Key
openai.api_key = 'your_api_key'

@app.route("/callback", methods=['POST'])
def callback():
    # Get request signature
    signature = request.headers['X-Line-Signature']

    # Get request body as text
    body = request.get_data(as_text=True)
    # Handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Check your channel secret and access token.")
        abort(400)

    return 'OK'

# This function handles message events from LINE
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    print(user_message)

    try:
        response = openai.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "你是一個基於繁體中文回應的幫手，請保持回應簡潔，不超過 100 個字。"},
            {"role": "user", "content": user_message}
        ]
        ) 
        print(response)
        reply_text = response.choices[0].message.content.strip()
    except Exception as e: 
        reply_text = "Sorry, I couldn't process your request."
        print(f"OpenAI API Error: {e}") 

    # Send reply message back to user
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )

if __name__ == "__main__":
    app.run(debug=True)
