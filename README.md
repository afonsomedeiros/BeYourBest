# BeYourBest
Projeto Integrador II

### TODO:
- [X] Criação de repositório.
- [X] Criação de estrutura do projeto.
- [ ] Importação de telas.
- [X] Criação de Modelos
- [ ] Criação de rotas da API para CRUD
- [ ] Criação de controllers para acesso aos dados.
- [ ] Criação de autenticação.

## 1 - Estrutura do projeto

```sh
├── LICENSE
├── README.md
├── __pycache__
│   └── application.cpython-38.pyc
├── app
│   ├── __init__.py
│   ├── __pycache__
│   │   └── __init__.cpython-38.pyc
│   ├── api
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-38.pyc
│   │   │   └── home.cpython-38.pyc
│   │   └── home.py
│   ├── extensions
│   │   └── __init__.py
│   ├── models
│   │   └── __init__.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-38.pyc
│   │   │   └── home_route.cpython-38.pyc
│   │   └── home_route.py
│   ├── serializers
│   │   └── __init__.py
│   └── templates
│       └── index.html
└── application.py
```

### 1.1 - Arquivos e Diretórios

Todos os arquivo **`__init__.py`** identificam a pasta onde eles estão como pacotes, isso ajuda o interpretador do python a localizar recursos.

Vão notar que no GitHub não existem as pastas pycache, estas pastas são geradas automaticamente toda vez que executamos o projeto, elas criam uma imagem dos arquivos compilados para melhorar a performance nas próximas execuções.

A pasta **controllers** é reponsável pela busca/entrega de informações para o cliente, é nela que criaremos o redirecionamento para todas as telas.

A pasta **api** irá conter recursos voltados a dados, é nesta pasta onde iremos adicionar recursos voltados a cadastro, atualização, validação e exclusão de dados.

A pasta **models** irá conter os modelos do projeto, estes modelos são "mapas" de tabela no banco de dados.

A Pasta **extensions** irá conter extensões necessárias para o projeto, como sqlalchemy, marshmallow, entre outros.

A pasta **serializers** é onde ficará os mapas de conversão dos modelos em arquivos (ficará mais claro quando começarmos a usar.)

A pasta **routes** tem uma função bem básica, linkar as funções das pastas **api** e **controllers** com um **endpoint** (ex: /usuarios/novo).

A pasta **templates** é onde ficarão disponíveis os códigos HTML do projeto.

A pasta **app** é a pasta do projeto.

Arquivo **application.py** é o ponto de inicio do projeto.

## 2 - Para execução do projeto.

Para executar esse projeto é necessário ter instalado no seu computador:

- [x] Python >= 3.7
- [x] Virtualenv

### 2.1 - Criando ambiente virtual e instalando pacotes.

Com virtualenv instalado basta executar o comando abaixo na pasta do projeto para criar um novo ambiente virtual.

Linux:

```sh
python3 -m virtualenv venv # criação do ambiente virtual.
source ./venv/bin/activate # para ativar ambiente virtual.
```

Windows:
```sh
virtualenv venv
./venv/Script/activate
```

Para instalar os pacotes basta executar o comando abaixo:

```
pip install -r requirements.txt
```

### 2.2 - Variaveis de ambiente para execução do projeto.

Definindo variaveis de ambiente em uma instancia local (nao há necessidade de criar variáveis de ambiente globais).

-- necessário para utilização do CLI para execução, criação do banco de dados e migrações.

Linux
```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True
```

Windows:
```sh
set FLASK_APP=app
set FLASK_ENV=Development
set FLASK_DEBUG=True
```

### 2.3 - Criando tabelas no banco de dados:

```sh
flask db init
flask db migrate
flask db upgrade
```

### 2.4 - Executando projeto.

1ª Forma:
```sh
python application.py
```

2ª Forma:
```sh
flask run
```