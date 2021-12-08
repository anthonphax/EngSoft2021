# Jornada 2021-02

[https://yt3.ggpht.com/ytc/AKedOLRt1d4p7bPylasq_66BIC8-k3hkyVjJ2JICQITK=s900-c-k-c0x00ffffff-no-rj](https://yt3.ggpht.com/ytc/AKedOLRt1d4p7bPylasq_66BIC8-k3hkyVjJ2JICQITK=s900-c-k-c0x00ffffff-no-rj)

## Setup do backend:

1. Instalar o Python e se certificar do funcionamento do pip:
2. Clonar o projeto localmente, usar o comando git checkout feature/loan, e puxar as dependências do mesmo com o comando abaixo: 
    
    ```bash
    pip install djangorestframework-simplejwt djangorestframework markdown django-filter
    ```
    
3. Na pasta raiz da aplicação, utilize os seguintes comandos comandos:
    
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
    
4. Após isto, execute o seguinte comando para rodar o backend da aplicação:
    
    ```bash
    python3 manage.py runserver
    ```
    
5. Com isto, a aplicação estará rodando em localhost, na porta 8000, sendo possível fazer as requisições através de plataformas como o Postman ou o Insomnia, ou até mesmo o navegador, onde na raiz é possível observar os endpoints existentes na aplicação.

O banco de dados é criado no momento das migrações e não está incluso no GitHub, portanto não possui dados, é possível povoá-lo através das plataformas citadas acima ou pelo navegador.