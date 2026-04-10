import sys
import os

# Ajusta o caminho para o Python reconhecer a pasta 'backend' como raiz
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, backend_dir)

# Agora importamos passando pelo pacote 'src'
from src.app import app 
from src.database import db
from src.models import Cliente, Profissional, Obra, Projeto

CLIENTES = [
    {"nome": "Construtora Alfa S/A", "cpf": "11122233344", "telefone": 11988887777},
    {"nome": "João Silva Investimentos", "cpf": "55566677788", "telefone": 11999990000}
]

PROFISSIONAIS = [
    {"categoria": "Engenheiro Civil", "nome": "Carlos Mendes", "num_crea": "123456/SP", "salario": 8500.00},
    {"categoria": "Arquiteta", "nome": "Ana Beatriz", "num_crea": "654321/SP", "salario": 7200.00}
]

OBRAS = [
    {"endereco": "Av. Paulista, 1000", "data_inicio": "2023-01-10", "previsao_final": "2024-12-20", "cliente": "Construtora Alfa S/A", "valor_contrato": 1500000.00, "nome_profissional": "Carlos Mendes"},
    {"endereco": "Rua das Flores, 123", "data_inicio": "2023-06-15", "previsao_final": "2024-03-10", "cliente": "João Silva Investimentos", "valor_contrato": 450000.00, "nome_profissional": "Ana Beatriz"}
]

PROJETOS = [
    {"categoria": "Estrutural", "data_contrato": "2022-11-05", "cliente": "Construtora Alfa S/A", "valor_contrato": 120000.00, "art": 500.00, "nome_profissional": "Carlos Mendes"},
    {"categoria": "Arquitetônico", "data_contrato": "2023-02-20", "cliente": "João Silva Investimentos", "valor_contrato": 80000.00, "art": 300.00, "nome_profissional": "Ana Beatriz"}
]

def seed():
    with app.app_context():
        db.create_all()
        
        if Cliente.query.first():
            print("Banco já populado")
            return

        print("Iniciando o povoamento do banco de dados de Obras...")

        print("- Inserindo Clientes...")
        for c in CLIENTES:
            db.session.add(Cliente(**c))

        print("- Inserindo Profissionais...")
        for p in PROFISSIONAIS:
            db.session.add(Profissional(**p))
            
        print("- Inserindo Obras...")
        for o in OBRAS:
            db.session.add(Obra(**o))
            
        print("- Inserindo Projetos...")
        for pr in PROJETOS:
            db.session.add(Projeto(**pr))
    
        db.session.commit()
        print("Seed finalizado com sucesso.")

if __name__ == '__main__':
    seed()