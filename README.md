# 🌳 Árvore Binária de Busca (ABB) com Interface Gráfica – CustomTkinter

Este projeto implementa uma Árvore Binária de Busca (ABB) em Python, com uma interface gráfica interativa construída usando Tkinter e CustomTkinter.

A aplicação permite:

➕ Adicionar elementos

🔍 Pesquisar elementos

➖ Eliminar elementos (com reconstrução balanceada automática)

🧩 Gerar a árvore de forma equilibrada na composição inicial

🖥️ Visualizar a estrutura da árvore em formato textual, incluindo os galhos, posições e hierarquia.

🚀 Funcionalidades
✔ Composição inicial

O usuário insere uma lista de valores (ex.: 15, 6, 18, 3, 7...)

A lista é ordenada automaticamente

A árvore é construída já balanceada, utilizando o elemento central como raiz e dividindo a lista recursivamente

✔ Operações disponíveis
🔍 Pesquisa (P)

Verifica se um valor está presente na árvore.

➕ Adição (A)

Insere um novo elemento

Após a inserção, a árvore é reconstruída para manter-se equilibrada

➖ Eliminação (E)

Remove um elemento existente

Reconstrói a árvore mantendo o balanceamento

✔ Visualização

A árvore é exibida como um desenho ASCII, representando nós, níveis, ramificações e hierarquia.

Exemplo:
```bash
       ___15____
      /         \
    _6_        _18_
   /   \      /    \
  3     7   17    20
```
🛠 Tecnologias Utilizadas

Python 3.x

Tkinter

CustomTkinter

Estruturas de dados (árvore binária de busca)

Recursão para:

Inserção

Busca

Impressão visual

Reconstrução balanceada

📦 Instalação
1. Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. Instale o CustomTkinter
pip install customtkinter

3. Execute o programa
python nome_do_arquivo.py

🖼 Interface

A interface contém:

Campo para valores iniciais

Botões de:

Compor/Reorganizar árvore

Executar operações

Radio buttons para selecionar o procedimento (P / A / E)

Área de texto mostrando a árvore

🧠 Lógica da Árvore

A classe principal EstruturaBuscaBinaria implementa:

Inserção recursiva

Busca recursiva

Percurso em ordem (in-order)

Reconstrução balanceada

Desenho ASCII estruturado

A classe Estrutura_Interface gerencia:

Entrada do usuário

Feedback visual

Execução dos procedimentos

Exibição da árvore

🗂 Estrutura do Código
```bash
📁 projeto/
 ├── 📄 main.py   → Código completo da árvore + interface
 └── 📄 README.md  → Este arquivo
```
🧪 Exemplo de Entrada
15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9, 10, 8, 16, 19


A aplicação automaticamente:

Ordena a lista

Constrói a árvore balanceada

Exibe a estrutura

✨ Características Especiais

🌈 Interface moderna com CustomTkinter (modo escuro)

🧩 Árvore sempre equilibrada após adições/remoções

🔄 Interface atualiza automaticamente após qualquer modificação

⚠️ Mensagens de erro, avisos e sucesso (coloridos)

📐 Impressão de árvore altamente legível
