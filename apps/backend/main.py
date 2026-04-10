import os
from dotenv import load_dotenv

load_dotenv()

from src.app import app

if __name__ == '__main__':
    print("Iniciando o servidor da API de Obras e Projetos...")
    app.run(debug=True, host='0.0.0.0', port=5000)