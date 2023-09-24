import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        app.secret_key = 'test_secret_key'  # Defina uma chave secreta para testes
        self.users = []  # Mova a lista de usuários para fora do objeto Flask

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_route(self):
        response = self.app.post('/login', data=dict(username='user1', password='password1'))
        self.assertEqual(response.status_code, 302)  # Deve redirecionar para o dashboard após o login

    def test_dashboard_route(self):
        # Adicione um usuário de teste à lista de usuários
        self.users.append({'username': 'user1', 'password': 'password1'})
        
        # Faça login antes de acessar o painel
        with self.app.session_transaction() as sess:
            sess['user'] = 'user1'
        
        response = self.app.get('/dashboard')
        self.assertEqual(response.status_code, 200)  # Deve retornar 200 OK

    def test_logout_route(self):
        response = self.app.get('/logout')
        self.assertEqual(response.status_code, 302)  # Deve redirecionar para a página inicial após o logout

    def test_register_route(self):
        response = self.app.post('/register', data=dict(username='user2', password='password2'))
        self.assertEqual(response.status_code, 200)  # Deve retornar 200 OK

if __name__ == '__main__':
    unittest.main()
