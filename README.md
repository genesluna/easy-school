# 🧑‍🏫 EasySchool

Este aplicativo foi concebido para a disciplina de back-end do curso ADS do CESMAC. O objetivo é criar um mini sistema de gerenciamento de escolas usando python e o framework Django.

Essa `branch (ea1)` está relacionada com a primeira parte do projeto que consiste dos seguintes passos:

### 📝 Passos

**Passo 1**:

- Criar o modelo `Aluno` com os campos:
  - `nome`
  - `sobrenome`
  - `email`

**Passo 2**:

- Criar o modelo `Curso` com os campos:
  - `titulo`
  - `descricao`
- Relacionamento: Um aluno pode estar matriculado em vários cursos.

**Passo 3**:

- Configurar o Django Admin para cadastrar alunos.
- Criar uma URL e uma view para exibir os alunos cadastrados.
- Criar templates para exibir a lista de alunos.

**Passo 4**:

- Configurar o Django Admin para cadastrar cursos.
- Criar uma URL e uma view para exibir os cursos cadastrados.
- Criar templates para exibir a lista de cursos.

## ⚙️ Instalação

1. Clone este repositório:

   ```bash
   git https://github.com/genesluna/easy-school.git
   cd easy-school
   ```

2. Crie um ambiente virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv/Scripts/Activate.ps1  # Windows Powershell
   ```

3. Atualizar o pip:

   ```bash
    pip install --upgrade pip
   ```

4. Instalar dependências:
   ```bash
    pip install -r requirements.txt
   ```
5. Execute as migrações para criar o banco de dados:

   ```bash
   python manage.py migrate
   ```

6. Crie um superusuário para acessar o Django Admin:

   ```bash
   python manage.py createsuperuser
   ```

7. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```
