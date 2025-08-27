# 📚 App Biblioteca — Django

## Problema
Instituições e cursos precisam de uma forma simples de **organizar o acervo**, **buscar artigos/livros** e **facilitar o acesso** a materiais acadêmicos.

## Solução
Uma aplicação web em **Django 4** que permite listar conteúdos, buscar por termos e exibir páginas de artigo, pronta para evoluir para um CRUD completo de acervo.

## Stack
- **Linguagem**: Python 3.x
- **Framework**: Django 4.1
- **Banco**: SQLite (padrão do projeto)
- **Gerenciador de dependências**: `pip` (arquivo `requirements.txt`)
- **Arquitetura**: apps Django (`biblioteca`) + projeto (`setup`)

## Como rodar
1) **Clonar** o repositório e entrar na pasta raiz:
```bash
cd tese-app-biblioteca-main
```
2) **Criar venv** e **instalar dependências**:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
3) **Aplicar migrações** do banco:
```bash
python manage.py migrate
```
4) (Opcional) **Criar usuário admin** para acessar o admin do Django:
```bash
python manage.py createsuperuser
```
5) **Subir o servidor** de desenvolvimento:
```bash
python manage.py runserver
```
A aplicação ficará disponível em **http://127.0.0.1:8000/**.

## Endpoints
| Método | Caminho   | Descrição                  |
| ------ | --------- | -------------------------- |
| GET    | `/`       | index (lista/landing)      |
| GET    | `/artigo` | artigo (página de artigo)  |
| GET    | `/buscar` | buscar (busca de conteúdo) |
