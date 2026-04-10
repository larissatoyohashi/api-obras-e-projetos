# 🏗️ API de Obras e Projetos

Uma API RESTful desenvolvida em Python e Flask para o gerenciamento de Clientes, Profissionais, Obras e Projetos. O projeto conta com validação de dados via Pydantic e documentação interativa automática gerada com Swagger.

## 🚀 Tecnologias Utilizadas

* **[Python](https://www.python.org/)** - Linguagem principal.
* **[Flask](https://flask.palletsprojects.com/)** - Framework web para a criação da API.
* **[SQLAlchemy](https://www.sqlalchemy.org/)** - ORM para manipulação e criação do banco de dados.
* **[Pydantic](https://docs.pydantic.dev/)** - Para criação de schemas e validação de requisições.
* **[Flasgger](https://github.com/flasgger/flasgger)** - Para a geração automática da documentação Swagger.

---

## 📋 Pré-requisitos

Certifique-se de ter o Python 3.x instalado na sua máquina e um terminal disponível para a execução dos comandos.

---

## 🔧 Como inicializar o projeto localmente

Siga o passo a passo abaixo para rodar a aplicação na sua máquina:

**1. Clone ou extraia o projeto**
Abra o terminal na pasta raiz do projeto (onde está localizado o arquivo `main.py`).

**2. Ative o ambiente virtual**
É recomendado rodar o projeto dentro de um ambiente isolado.
* No Windows:
  > .\.venv\Scripts\activate
* No Mac/Linux:
  > source .venv/bin/activate

**3. Instale as dependências**
Com o ambiente ativado, copie e cole o comando abaixo no terminal para instalar todas as bibliotecas necessárias de uma só vez:
> pip install Flask Flask-SQLAlchemy pydantic flasgger python-dotenv

**4. Configure as Variáveis de Ambiente**
* Crie um arquivo chamado `.env` na raiz do projeto.
* Copie todo o conteúdo do arquivo `.env.example` e cole dentro do `.env`.
* Ajuste os valores caso necessário.

**5. Popule o Banco de Dados (Opcional)**
Se for a primeira vez rodando o projeto ou se quiser iniciar com dados de teste pré-cadastrados, execute o script de inserção:
> python src/scripts/seed.py

**6. Inicie o Servidor**
Rode o arquivo principal para colocar a API no ar:
> python main.py

---

## 📖 Documentação Interativa (Swagger)

A API possui uma interface visual onde você pode testar todas as rotas (GET, POST, PUT, DELETE) diretamente pelo navegador.

Com o servidor rodando (Passo 6 concluído), acesse o link abaixo:
👉 **[http://127.0.0.1:5000/apidocs](http://127.0.0.1:5000/apidocs)**