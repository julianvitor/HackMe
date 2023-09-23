from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Troque isso por uma chave secreta segura

# Lista para armazenar os usuários cadastrados (simples para fins de demonstração)
users = []

@app.route('/')
def home():
    if 'user' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    for user in users:
        if user['username'] == username and user['password'] == password:
            session['user'] = username
            return redirect(url_for('dashboard'))
    
    return "Login falhou. Verifique suas credenciais."

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', users=users)
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Verificar se o usuário já está cadastrado
        for user in users:
            if user['username'] == username:
                return "Nome de usuário já existe."
        
        # Adicionar o novo usuário à lista
        new_user = {'username': username, 'password': password}
        users.append(new_user)
        print(users)
        return "Cadastro bem-sucedido. Faça login agora."
    
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
