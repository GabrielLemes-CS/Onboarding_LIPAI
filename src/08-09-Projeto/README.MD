# Projeto A - Sistema de Gestão de Alunos e Projetos de IC

## 📋 Descrição
Este projeto consiste em um sistema em linha de comando (CLI) desenvolvido em Python para gerenciar alunos, projetos de Iniciação Científica (IC) e suas respectivas participações. O objetivo é facilitar o controle acadêmico, permitindo o registro e a consulta rápida de vínculos entre estudantes e projetos de pesquisa.

O sistema foi desenvolvido como parte das atividades de avaliação da disciplina de LIPAI / Onboarding.

## Funcionalidades
O sistema atende aos seguintes requisitos funcionais:

* **Gerenciamento de Alunos:**
    * Cadastrar novos alunos (Prontuário, Nome, Email).
    * Listar todos os alunos cadastrados.
    * Buscar aluno por prontuário.
* **Gerenciamento de Projetos:**
    * Cadastrar novos projetos (Código, Título, Responsável).
    * Listar todos os projetos.
    * Buscar projeto por código.
* **Gerenciamento de Participações:**
    * Registrar a participação de um aluno em um projeto (com data de início e fim).
    * Validar a existência do aluno e do projeto antes do cadastro.
* **Relatórios e Buscas:**
    * Listar todas as participações de um aluno específico.
    * Listar todos os alunos vinculados a um projeto específico.
* **Persistência de Dados:**
    * Todos os dados são salvos automaticamente em arquivos CSV na pasta `data/`.

## 📂 Estrutura do Projeto
O código está organizado da seguinte forma para garantir a modularização:

├── data/                  # Diretório onde os arquivos .csv são salvos
│   ├── alunos.csv
│   ├── projetos.csv
│   └── participacoes.csv
├── main.py                # Ponto de entrada da aplicação
├── menus.py               # Interface de menus e interação com o usuário
├── models.py              # Definição das classes (Aluno, Projeto, Participacao)
├── repositorios.py        # Lógica de negócio e leitura/escrita de arquivos
└── README.md              # Documentação do projeto

## 🛠️ Pré-requisitos
Para executar este projeto, você precisa ter instalado:
* [Python 3.x](https://www.python.org/downloads/)

## ▶️ Como Executar
Siga os passos abaixo para rodar o projeto na sua máquina:

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git](https://github.com/SEU-USUARIO/NOME-DO-REPOSITORIO.git)
    ```

2.  **Acesse a pasta do projeto:**
    ```bash
    cd NOME-DO-REPOSITORIO
    ```

3.  **Execute o arquivo principal:**
    ```bash
    python main.py
    ```
    *(Nota: O sistema criará a pasta `data/` e os arquivos CSV automaticamente caso eles não existam na primeira execução, se a lógica estiver implementada, ou certifique-se de criar a pasta `data` manualmente).*

## ✒️ Autor
* **[Seu Nome Completo]** - *Desenvolvimento*