# FastSQL 👻

<p align="center">
<img width="250" height="300" alt="image" src="https://github.com/user-attachments/assets/4ebdb7ac-6a5a-42ca-a391-cd4fd2a5d18e" />
</p>

Projeto FastAPI + SQLModel com rate limiting e leitura de variáveis de ambiente para conectar ao banco de dados.

## Visão geral da arquitetura

```
FastSql/
├── main.py              # Ponto de entrada do servidor
├── requirements.txt     # Dependências do projeto
├── README.md            # Documentação do projeto
├── src/
│   ├── database/
│   │   └── .env         # Configuração do banco de dados
│   ├── Execet/
│   │   └── lerEnv.py     # Carrega a variável de ambiente do .env
│   ├── LimiteIp/
│   │   └── ratelimite.py # Configura rate limiter
│   ├── Model/
│   │   └── model.py      # Define o modelo Cliente (SQLModel)
│   ├── routes/
│   │   └── User.py       # Rotas da API para usuário
│   └── server/
│       └── Server.py     # Configura o FastAPI e registra rotas
```

## Como funciona

- `main.py` cria a aplicação FastAPI, conecta ao banco de dados e registra as rotas de usuário.
- `src/Execet/lerEnv.py` carrega a URL do banco de dados do arquivo `src/database/.env`.
- `src/Model/model.py` define a tabela `Cliente` com campos `id`, `nome` e `senha`.
- `src/routes/User.py` define as rotas:
  - `POST /creat` para criar um novo usuário
  - `GET /users` para listar todos os usuários
  - `GET /userverfy` para verificar login
- `src/LimiteIp/ratelimite.py` configura o rate limiter usado nas rotas.
- `src/server/Server.py` instancia `FastAPI` e fornece métodos simples para registrar rotas.

## Onde colocar o banco de dados

O arquivo de configuração do banco de dados fica em:

- `src/database/.env`

Exemplo de conteúdo do `.env`:

```env
db="sqlite:///./dados.db"
```

> Se você usar SQLite, o valor de `db` deve ser uma URL como `sqlite:///./dados.db`.
> Para outros bancos, use a URL de conexão completa do SQLAlchemy.

### Passos para configurar

1. Abra `src/database/.env`
2. Altere a linha `db = "SEU BANCO DE DADOS"` para a URL do seu banco
3. Salve o arquivo

## Instalação

1. Crie um ambiente virtual (recomendado):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Execução

Execute o servidor com:

```bash
python main.py
```

O servidor ficará disponível em `http://0.0.0.0:8000`.

## Observações importantes

- Não edite `main.py` se quiser manter a entrada padrão do servidor.
- Use `src/database/.env` para configurar apenas a string de conexão.
- O projeto espera que o valor `db` seja lido com `python-dotenv`.
