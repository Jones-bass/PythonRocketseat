# API de Pedidos

API em Flask para cadastro de usuários, login com JWT e criação de pedidos.

## Como rodar

1. Crie o ambiente virtual
python -m venv venv

2. Ative o ambiente
venv\Scripts\activate

3. Instale as dependências
pip install -r requirements.txt

4. Configure o .env
KEY=sua_chave
ALGORITHM=HS256
JWT_HOURS=10

5. Rode o projeto
python run.py


POST /registry
{
  "username": "joao",
  "email": "joao@email.com",
  "password": "12345678"
}


POST /login
{
  "email": "joao@email.com",
  "password": "12345678"
}

POST /orders
Authorization: Bearer TOKEN_AQUI

{
  "product_name": "Mouse",
  "quantity": 2
}


GET /orders
Authorization: Bearer TOKEN_AQUI
{
    "data": {
        "attributes": [
            {
                "id": 12,
                "product_name": "Notebook",
                "quantity": 2,
                "user_id": 20
            },
        ],
        "count": 3,
        "type": "Orders"
    }
}

