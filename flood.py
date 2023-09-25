import requests

class Flood:
    def __init__(self):
        # Informe ao usuário o que a aplicação fará
        print("Esta aplicação fará cadastros em uma aplicação Flask em loop.")
        print("Informe o endereço da sua aplicação Flask (por exemplo, http://localhost:5000/register):")
        self.url = input("Endereço da aplicação: ")

        # Solicite o número máximo de iterações ao usuário
        try:
            self.max_iterations = int(input("Número máximo de iterações: "))
        except ValueError:
            print("Insira um número válido para o número máximo de iterações.")
            exit(1)

    def fazer_cadastros(self):
        # Faça cadastro em loop com usuários e senhas crescentes
        for i in range(1, self.max_iterations + 1):
            # Construir o nome de usuário e senha com base na iteração
            username = 'a' * i
            password = 'a' * i

            data = {'username': username, 'password': password}

            response = requests.post(self.url, data=data)
            if response.status_code == 200:
                print(f"Cadastro bem-sucedido para o usuário: {username} | Senha: {password}")
            else:
                print(f"Falha ao cadastrar para o usuário: {username}")

if __name__ == '__main__':
    app = Flood()
    app.fazer_cadastros()
