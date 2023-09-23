import requests
import random
import string

# URL da sua aplicação Flask
base_url = 'http://localhost:5000'

# Número de usuários aleatórios que você deseja cadastrar
num_users = 10000

# Faça cadastro em loop com valores aleatórios
for _ in range(num_users):
    # Gerar um nome de usuário aleatório de 8 caracteres
    username = ''.join(random.choices(string.ascii_lowercase, k=1000))
    
    # Gerar uma senha aleatória de 10 caracteres
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=1000))
    
    data = {'username': username, 'password': password}
    
    response = requests.post(f'{base_url}/register', data=data)
    if response.status_code == 200:
        print(f"Cadastro bem-sucedido para {username} com senha {password}")
    else:
        print(f"Falha no cadastro para {username}")

# Após o loop de cadastro, você pode fazer login ou realizar outras ações conforme necessário
