# 🌳 Árvore Binária de Busca (ABB) com Interface Gráfica – CustomTkinter

Este projeto implementa uma Árvore Binária de Busca (ABB) em Python com uma interface gráfica moderna construída utilizando Tkinter e CustomTkinter.

# A aplicação permite:

➕ Adicionar elementos

🔍 Pesquisar elementos

➖ Eliminar elementos (com reconstrução balanceada automática)

🧩 Gerar a árvore já equilibrada na composição inicial

🖥️ Visualizar a estrutura da árvore em formato ASCII, incluindo galhos, posições e hierarquia

# 🚀 Funcionalidades
✔ Composição Inicial

O usuário insere uma lista de valores (ex.: 15, 6, 18, 3, 7...)

Os valores são automaticamente ordenados

A árvore é construída balanceada, escolhendo o elemento central como raiz

✔ Operações Disponíveis
🔍 Pesquisar (P)

Verifica se um valor está presente na árvore.

➕ Adicionar (A)

Insere um novo elemento

Após isso a árvore é reconstruída e equilibrada

➖ Eliminar (E)

Remove um elemento

A estrutura é recriada para manter o balanceamento

# ✔ Visualização Estruturada

A árvore é exibida como um desenho ASCII, com nós, níveis e ramificações.

Exemplo:
```bash

       ___15____
      /         \
    _6_        _18_
   /   \      /    \
  3     7   17    20
```

# 🛠 Tecnologias Utilizadas

Python 3.x

Tkinter

CustomTkinter

Estruturas de dados (Árvore Binária de Busca)

Recursão para busca, inserção, impressão e balanceamento

# 📦 Instalação
# 1. Instale as dependências #
O projeto inclui um arquivo requirements.txt, contendo:
customtkinter

# Instale com: #
pip install -r requirements.txt

# 2. Execute o programa # 
python main.py

🖼 Interface da Aplicação

Entrada de valores iniciais

Botão para compor/reorganizar a árvore

Seleção de operações (Pesquisar, Adicionar, Eliminar)

Campo para inserir o valor da operação

Exibição da árvore ASCII em tempo real

# 🧠 Lógica da Árvore
Classe EstruturaBuscaBinaria

Implementa:

Inserção recursiva

Busca recursiva

Travessia in-order

Balanceamento completo da árvore

Impressão ASCII detalhada

Classe Estrutura_Interface

Gerencia:

Entradas do usuário

Mensagens e feedback visual

Execução das operações (P / A / E)

Atualização da área de visualização

# 🗂 Estrutura do Projeto
```bash
📁 projeto/
 ├── 📄 main.py            → Código completo da árvore + interface
 ├── 📄 requirements.txt   → Lista de dependências
 └── 📄 README.md          → Este arquivo
```

🧪 Exemplo de Entrada
# 15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9, 10, 8, 16, 19 #
# A aplicação automaticamente:

Ordena os valores

Gera uma árvore balanceada

Exibe a estrutura visualmente

✨ Características Especiais

🌈 Interface moderna com CustomTkinter (modo escuro)

🧩 Árvore sempre equilibrada após qualquer modificação

🔄 Atualização instantânea da interface

⚠️ Mensagens coloridas (erro, aviso, sucesso)

📐 Impressão ASCII altamente legível
