# Ternos.com - Aplicação Web de E-commerce

O Ternos.com é uma aplicação web simples de e-commerce construída usando Python e Streamlit. Esta aplicação permite aos usuários navegar, visualizar e comprar produtos, bem como gerenciar seus perfis. Os usuários podem fazer login, se registrar e atualizar suas informações de perfil. O site pode ser acessado em [ternostore.streamlit.app](https://ternostore.streamlit.app/)

## Sumário

- [Recursos](#recursos)
- [Instalação](#instalação)
- [Utilização](#utilização)
- [Login de Usuário](#login-de-usuário)
- [Catálogo de Produtos](#catálogo-de-produtos)
- [Visualização e Limpeza do Carrinho](#visualização-e-limpeza-do-carrinho)
- [Gerenciamento de Perfil de Usuário](#gerenciamento-de-perfil-de-usuário)

## Recursos
- Autenticação e registro de usuário.
- Navegação e visualização de um catálogo de produtos.
- Adição de produtos ao carrinho de compras.
- Visualização do preço total dos itens no carrinho.
- Atualização das informações de perfil do usuário.
- Compra de produtos (simplificada).
- Logout.


## Instalação

Para instalar o projeto, siga estas etapas:

1. Clone o repositório:
```bash
git clone https://github.com/HenriqueAccorinti/ProjetoSemestralPOO.git
```
3. Acesse o diretório do projeto:
```bash
cd yourproject
```
5. Instale as dependências necessárias:
```
pip install streamlit
```
  - Se tiver dúvidas sobre como utilizar a biblioteca Streamlit, consulte https://docs.streamlit.io/library/get-started

## Utilização

Para executar a aplicação, execute o seguinte comando:
```bash
streamlit run main.py
```
## Login de Usuário

- Os usuários podem fazer login usando seu e-mail e senha.
- Se eles não tiverem uma conta criada, podem clicar no botão "Registrar-se" para criar uma.

### Registro

1. Clique no botão "Registrar-se".
2. Preencha as informações necessárias: Nome, E-mail, Senha e CPF.
3. Clique no botão "Cadastrar" para criar uma conta.

### Fazendo Login

1. Insira seu E-mail e Senha registrados.
2. Clique no botão "Entrar" para fazer login.

## Catálogo de Produtos

Após fazer o login, os usuários podem:

### Navegar por Produtos

Os produtos são exibidos com seus nomes, preços e uma imagem.
Clique no botão de um produto para adicioná-lo ao seu carrinho.

### Adicionar Produtos ao Carrinho

Especifique a quantidade que deseja comprar.
Clique no botão "Adicionar" para adicionar o produto ao seu carrinho.
Observe que a quantidade é limitada pelo estoque disponível do produto.

## Visualização e Limpeza do Carrinho

Na guia "🛒 | Carrinho", os usuários podem:

### Ver Carrinho

O carrinho exibe o nome do produto, o preço e a quantidade.
Você pode ver o preço total dos itens em seu carrinho.

### Limpar Carrinho
Para limpar seu carrinho e concluir sua compra, clique no botão "Finalizar Pedido".

## Gerenciamento de Perfil de Usuário

Os usuários podem gerenciar seu perfil clicando no ícone de usuário no canto superior esquerdo. Você pode:

### Ver Informações de Perfil

Veja seu Nome, E-mail e CPF.

### Alterar Informações de Login

1. Clique no botão "Mudar informações de login" para atualizar seu e-mail e senha.
2. Insira seu E-mail registrado e digite uma nova senha.

### Sair

Clique no botão "Sair" para sair de sua conta.
