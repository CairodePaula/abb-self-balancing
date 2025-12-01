# 🌌 Árvore Binária de Busca com Interface Gráfica
### CustomTkinter • NetworkX • Matplotlib • Python

### Uma aplicação visual interativa para manipulação e analisar o comportamento de uma Árvore Binária de Busca (ABB) balanceada.
### Desenvolvida com Tkinter + CustomTkinter e visualização gráfica por NetworkX e Matplotlib, a ferramenta permite criar, reorganizar e explorar árvores de forma intuitiva e dinâmica.

# 🔥 Recursos Principais
### 🌱 Composição Inicial Inteligente

Recebe uma lista de valores numéricos

Remove duplicações e ordena automaticamente

Constrói uma árvore totalmente balanceada desde o início

# ⚙️ Operações Disponíveis
🔍 Pesquisar

Verifica se o valor está na árvore

O nó encontrado é realçado visualmente

➕ Adicionar

Insere um novo valor

Reequilibra toda a estrutura automaticamente

➖ Eliminar

Remove um valor informado

Reconstrói a árvore de forma balanceada com os valores restantes

## 🔭 Visualização Gráfica em Tempo Real

A árvore é exibida como um grafo dinâmico, incluindo:

Nós grandes e destacados

Cores diferentes para operações (ex.: pesquisa)

Hierarquia respeitando profundidade e ramificação

Redesenho automático após qualquer ação

Tudo integrado diretamente na interface via Matplotlib + Tkinter.

## 🧠 Estrutura Interna
✨ Classe EstruturaBuscaBinaria

Implementa:

Inserção recursiva

Busca recursiva

Travessia in-order

Reconstrução balanceada

Exportação da árvore para um grafo NetworkX

## 🎨 Classe Estrutura_Interface

Responsável por:

Interface gráfica com CustomTkinter

Entrada de valores e validação

Controle das operações (Pesquisar, Adicionar, Eliminar)

Atualização do grafo na tela

Feedback visual colorido

# 🛠 Tecnologias Utilizadas

Python 3.x

Tkinter

CustomTkinter

NetworkX

Matplotlib

Programação orientada a objetos

Recursão em estruturas de dados

# 📦 Instalação
###1. Instale as dependências
pip install -r requirements.txt

### 2. Execute a aplicação
python main.py

## 🗂 Estrutura do Projeto
```bash
📁 projeto/
 ├── main.py               # Código da árvore + interface gráfica
 ├── requirements.txt      # Dependências
 └── README.md             # Documento atual
```
## 🧪 Exemplo de Entrada
```bash
15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9, 10, 8, 16, 19
```

A aplicação irá:

Remover duplicados

Ordenar

Criar automaticamente uma ABB equilibrada

Exibir graficamente

##✨ Destaques

Interface moderna com modo escuro

Árvore sempre balanceada após qualquer modificação

Visualização clara e responsiva

Mensagens coloridas (erro, aviso e sucesso)

Manipulação extremamente intuitiva
