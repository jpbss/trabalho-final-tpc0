# Sistema de Gestão de Oficina (Trabalho Final)

Este projeto é uma aplicação web desenvolvida em Python como trabalho final para a matéria eletiva de Tópicos em Programação durante minha graduação. A aplicação simula um sistema de gerenciamento para uma oficina ou revenda de veículos, permitindo o controle de clientes, veículos, serviços e transações financeiras.

## 1\. Visão Geral

O sistema permite que o usuário realize operações CRUD (Create, Read, Update e Delete) para as principais entidades de negócio de uma oficina, incluindo:

  * **Gestão de Clientes:** Cadastro de compradores e vendedores.
  * **Gestão de Prestadores:** Cadastro de empresas que fornecem serviços (ex: mecânicos, funilaria).
  * **Gestão de Veículos:** Registro detalhado de veículos em estoque, incluindo preços e características.
  * **Gestão de Despesas:** Lançamento de despesas (serviços) associadas a um veículo, vinculando-o a um prestador.
  * **Gestão de Compras:** Registro de operações de compra de veículos.
  * **Gestão de Vendas:** Registro de operações de venda de veículos.

## 2\. Pilha Tecnológica (Tech Stack)

  * **Backend:** Python 3
  * **Framework Web:** Flask
  * **Banco de Dados:** MySQL
  * **Frontend:** HTML, CSS e Jinja2 (Templates)

## 3\. Estrutura do Projeto

O projeto segue uma arquitetura que separa as responsabilidades (semelhante ao padrão MVC):

  * **`app.py`**: Ponto de entrada da aplicação Flask. Responsável por inicializar o app e registrar todas as rotas (Blueprints).
  * **`modelo/`**: Contém as classes que representam as entidades do banco de dados (ex: `cliente.py`, `veiculo.py`, `despesa.py`). Estas classes definem os atributos dos objetos e também geram os fragmentos SQL para as operações de CRUD.
  * **`controle/`**: Contém a lógica de negócio e as classes que fazem a ponte entre a visão e o banco de dados.
      * `conectarbanco.py`: Classe que gerencia a conexão com o MySQL.
      * `controleGenerico.py`: Classe base com métodos genéricos de CRUD (`incluir`, `alterar`, `delete`) que é herdada pelos outros controladores.
      * Controladores específicos (ex: `controleVeiculo.py`, `controleCliente.py`): Implementam a lógica para cada módulo, convertendo dados da web para objetos e vice-versa.
  * **`visao/`**: Define os *endpoints* (rotas) da aplicação usando Blueprints do Flask. Cada ficheiro (ex: `rotasVeiculo.py`) agrupa as URLs de um módulo e lida com as requisições HTTP, renderizando os templates adequados.
  * **`templates/`**: Ficheiros HTML (Jinja2) que compõem a interface do usuário.
  * **`static/`**: Contém ficheiros estáticos (CSS, JS, imagens).
  * **`sql-script.sql`**: Script DDL para criação do banco de dados `oficina` e suas tabelas.

## 4\. Como Executar

1.  **Configurar o Banco de Dados:**

      * Certifique-se de ter um servidor MySQL em execução.
      * Execute o script `sql-script.sql` para criar o banco `oficina` e as tabelas necessárias.
      * **Importante:** Atualize as credenciais de conexão no ficheiro `controle/controleGenerico.py` (host, usuário, senha) de acordo com a sua configuração local.

2.  **Instalar Dependências:**
    (Recomenda-se usar um ambiente virtual `venv`)

    ```bash
    pip install Flask mysql-connector-python
    ```

3.  **Iniciar a Aplicação:**

    ```bash
    python app.py
    ```

4.  **Entrar no Sistema:**
    Abra o seu navegador em `http://127.0.0.1:5000`.
