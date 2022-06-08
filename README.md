# BeYourBest
Projeto Integrador II

### TODO:
- [X] Criação de repositório.
- [X] Criação de estrutura do projeto.
- [ ] Importação de telas.
- [ ] Criação de Modelos
- [ ] Criação de rotas da API para CRUD
- [ ] Criação de controllers para acesso aos dados.
- [ ] Criação de autenticação.

### Estrutura do projeto

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

### Para execução do projeto.

Antes de executar o projeto deve instalar as dependencias. Lembre-se de utilizar um ambiente virtual, para não poluir a instalação do python da sua máquina. Para instalar basta executar o comando abaixo.

```sh
pip install -r requirements.txt
```

Depois, para executar o projeto execute o comando abaixo:

```sh
python application.py
```