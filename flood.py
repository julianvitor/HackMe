import requests

# URL da sua aplicação Flask
base_url = 'http://localhost:5000'

# Número máximo de iterações
max_iterations = 1000000000000000

# Faça cadastro em loop com usuários e senhas crescentes
for i in range(100000000, max_iterations + 1):
    # Construir o nome de usuário e senha com base na iteração
    username = 'a' * i
    password = 'a' * i
    
    data = {'username': username, 'password': password}
    
    response = requests.post(f'{base_url}/register', data=data)
    if response.status_code == 200:
        print(f"{username}{password}")
    else:
        print(f"Falha")

# Após o loop de cadastro, você pode fazer login ou realizar outras ações conforme necessário
