# Lista-Compras
Projeto simples em FastAPI para gerenciar uma lista de compras, permitindo inserir, listar, alterar status e deletar itens de forma prática via API REST.

- Tecnologias utilizadas

    Python 3

    FastAPI (criação de API REST de forma rápida e tipada)

    Pydantic (validação e tipagem de dados)

    Uvicorn (servidor ASGI para FastAPI)

-  Funcionalidades

    Inserir novas compras com produto, quantidade, preço e data
    Listar todas as compras ou filtrar por realizadas/não realizadas
    Visualizar uma compra específica por índice
    Alterar o status de realizada/não realizada
    Deletar compras da lista

⚙️ Como executar localmente

Clone este repositório:

git clone https://github.com/JallsBR/Lista-Compras.git
cd fastapi-lista-compras

2️⃣ Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv

- Windows
venv\Scripts\activate

- Linux/Mac
source venv/bin/activate

3️⃣ Instale as dependências:

pip install -r requirements.txt

4️⃣ Execute o servidor:

uvicorn main:app --reload

5️⃣ Acesse a documentação interativa:

    localhost/docs (Swagger)