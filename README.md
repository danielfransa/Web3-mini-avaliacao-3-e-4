# Web3-mini-avaliacao-3-e-4
Mini-atividade #4 e #5 - Da aula de Web 3 criado um aplicativo To Do com Django

Página inicial do projeto trazendo todas as tarefas cadastradas:

![pagina inicial](https://user-images.githubusercontent.com/102123924/236437831-f0de80be-08ab-465a-bf27-35c3af37d36a.png)

Página de cadastro de novas tarefas:

![image](https://user-images.githubusercontent.com/102123924/236438144-0fb1703b-aa48-45f9-846e-2e3aae2f75ae.png)


Django Admin ajustado para fazer controle das tarefas:

![image](https://user-images.githubusercontent.com/102123924/236438493-785485c9-2c20-4d54-bdcc-99d4bad6c38e.png)
<br>
![image](https://user-images.githubusercontent.com/102123924/236438642-3cf17302-2a07-4d3d-88f6-121dcd96af1a.png)


Para rodar o projeto criar um ambiente de desenvolvimento com virtualenv:

**Instalar virtualenv**

rodar esse comando no prompt de comando:

`pip install virtualenv`

depois no prompt de comando seguir os passos abaixo:

### Criar e ativar ambiente virtual:
================================

- virtualenv ambiente1
- ou digite:
- python -m virtualenv ambiente1
- cd ambiente1
- cd Scripts
- activate.bat

depois de entra ativar o ambiente colar os arquivos do GIT e rodar o comando abaixo no prompt de comando:

`pip install -r requirements.txt`

Entrar na pasta to_do e executar o comando abaixo para rodar a migrate e o servidor:

- `python manage.py migrate`

- `python manage.py runserver`

No navegador entrar no endereço 127.0.0.1:8000

para o Django Admin ver abaixo:

Senha para o Django Admin é uma senha genérica apenas para fins acadêmicos sendo ela:

Usuário | Senha
|--------|-------|
Admin | 123mudar


