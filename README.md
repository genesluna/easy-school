# 🧑‍🏫 EasySchool (EA3)

Este aplicativo foi concebido para a disciplina de back-end do curso de ADS do CESMAC. O objetivo é criar um mini sistema de gerenciamento de escolas usando python e o framework Django.

Essa `branch (ea3)` está relacionada à terceira parte do projeto que consiste dos seguintes passos:

### 📝 Passos

**Passo 1**:

**Qual a diferença entre as estruturas de banco de dados SQL e NoSQL? Aponte suas vantagens e desvantagens.**

Os bancos SQL (Structured Query Language) são relacionais, organizados em tabelas com estrutura rígida e relacionamentos bem definidos entre si. Eles garantem consistência dos dados através das propriedades ACID (Atomicidade, Consistência, Isolamento e Durabilidade) e são ideais para aplicações que exigem integridade rigorosa, como sistemas financeiros ou de gestão empresarial.

Já os bancos NoSQL (Not Only SQL) possuem estrutura flexível, permitindo armazenar dados sem um esquema predefinido. Podem ser baseados em documentos, chave-valor, grafos ou colunas. São mais escaláveis horizontalmente e adequados para grandes volumes de dados não estruturados, como em redes sociais ou análise de dados em tempo real.

As principais vantagens do SQL incluem consistência forte dos dados, suporte a transações complexas e linguagem padronizada. Suas desvantagens são menor flexibilidade para mudanças na estrutura e limitações de escala horizontal. Para o NoSQL, as vantagens são alta flexibilidade, melhor performance em grandes volumes de dados e facilidade de escala. Como desvantagens, apresenta consistência eventual (menos rigorosa) e falta de padronização entre diferentes soluções.

**Passo 2**:

Com base na tabela abaixo, gere o json equivalente.

**Usuários**

| Nome   | Email            |
| :----- | :--------------- |
| Carlos | carlos@email.com |
| João   | joao@email.com   |

**Resposta:**

```json
{
  "usuarios": [
    {
      "nome": "Carlos",
      "email": "carlos@email.com"
    },
    {
      "nome": "João",
      "email": "joao@email.com"
    }
  ]
}
```

**Passo 3**:

Utilizando Django Rest Framework, crie uma API para retornar os dados do passo 2

**Passo 4**:

**Explique, com suas palavras, o fluxo de uma autenticação com JWT. Pesquise sobre Simple JWT no django e crie uma rota para gerar e validar os tokens.**

O JWT (JSON Web Token) funciona como um sistema de autenticação baseado em tokens. O fluxo começa quando um usuário faz login com suas credenciais. O servidor valida essas informações e, se corretas, gera um token JWT contendo dados do usuário (payload), assinado com uma chave secreta. Este token é então enviado ao cliente, que o armazena localmente e o utiliza em todas as requisições subsequentes através do cabeçalho de autorização.

Quando o cliente faz uma nova requisição, o servidor verifica a autenticidade do token através da assinatura e valida se ele não está expirado. Se válido, o servidor permite o acesso aos recursos solicitados. Como o token contém as informações do usuário, não é necessário consultar o banco de dados a cada requisição.

As principais vantagens do JWT incluem sua natureza stateless (o servidor não precisa armazenar sessões), facilidade de escalar horizontalmente, possibilidade de uso entre diferentes domínios e serviços, e eficiência nas requisições. Como desvantagens, destacam-se a impossibilidade de invalidar um token específico antes de sua expiração (exceto com implementações adicionais), o tamanho maior dos tokens em comparação com sessões tradicionais, e riscos de segurança se a chave secreta for comprometida ou se o token for armazenado inadequadamente no cliente.

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
