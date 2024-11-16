# 🧑‍🏫 EasySchool

Este aplicativo foi concebido para a disciplina de back-end do curso de ADS do CESMAC. O objetivo é criar um mini sistema de gerenciamento de escolas usando python e o framework Django.

Essa `branch (ea2)` está relacionada à segunda parte do projeto que consiste dos seguintes passos:

### 📝 Passos

**Passo 1**:

- Crie o modelo de `Produto` em models.py com os seguintes atributos::
  - `nome`
  - `descrição`
  - `preço`
  - `validade`

**Passo 2**:

- Agora, devemos construir nosso template geral chamado `base.html`. Crie o template `base.html` contendo um bloco (block) chamado content.

**Passo 3**:

- Devemos poder cadastrar novos produtos no sistema sem ser pelo Django Admin.
- Crie um formulário em forms.py chamado ProdutoForm com os respectivos dados do modelo.

**Passo 4**:

- Por fim, devemos criar em views.py uma view (função) chamada:

  produto_new(request): …

- Nesta view, carregue o formulário e insira no banco de dados as informações necessárias

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
