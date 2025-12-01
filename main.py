import tkinter as tk
from tkinter import messagebox
from customtkinter import *

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Vertice:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None

class EstruturaBuscaBinaria:
    def __init__(self):
        self.ponto_inicial = None

    def adicionar_dado(self, dado):
        self.ponto_inicial = self._adicionar_recursivo(self.ponto_inicial, dado)

    def _adicionar_recursivo(self, vertice, dado):
        if vertice is None: return Vertice(dado)
        if dado < vertice.dado:
            vertice.esquerda = self._adicionar_recursivo(vertice.esquerda, dado)
        elif dado > vertice.dado:
            vertice.direita = self._adicionar_recursivo(vertice.direita, dado)
        return vertice

    def buscar_dado(self, dado): return self._buscar_recursivo(self.ponto_inicial, dado)

    def _buscar_recursivo(self, vertice, dado):
        if vertice is None or vertice.dado == dado: return vertice is not None
        if dado < vertice.dado: return self._buscar_recursivo(vertice.esquerda, dado)
        return self._buscar_recursivo(vertice.direita, dado)

    def obter_elementos_em_ordem(self):
        elementos = []
        self._percurso_em_ordem(self.ponto_inicial, elementos)
        return elementos

    def _percurso_em_ordem(self, vertice, elementos):
        if vertice:
            self._percurso_em_ordem(vertice.esquerda, elementos)
            elementos.append(vertice.dado)
            self._percurso_em_ordem(vertice.direita, elementos)
    
    def _compor_estrutura_balanceada_recursiva(self, elementos):
        if not elementos: return None
        meio = len(elementos) // 2
        vertice_inicio = Vertice(elementos[meio])
        vertice_inicio.esquerda = self._compor_estrutura_balanceada_recursiva(elementos[:meio])
        vertice_inicio.direita = self._compor_estrutura_balanceada_recursiva(elementos[meio + 1:])
        return vertice_inicio

    def eliminar(self, dado):
        if not self.buscar_dado(dado):
            return False, f"❌ Dado {dado} indisponivel para eliminacao."
            
        lista_ordenada = self.obter_elementos_em_ordem()
        try:
             lista_ordenada.remove(dado)
        except ValueError:
            return False, f"❌ Erro ao remover {dado}."
        
        self.ponto_inicial = None
        self.ponto_inicial = self._compor_estrutura_balanceada_recursiva(lista_ordenada)
        return True, f"✅ Dado {dado} eliminado e o arranjo foi refeito/equilibrado."
    
    def gerar_grafo(self):
        G = nx.DiGraph()
        def adicionar_vertice_e_arestas(vertice, pai=None, relacao=None):
            if vertice:
                G.add_node(vertice.dado)
                if pai is not None:
                    G.add_edge(pai.dado, vertice.dado, relacao=relacao)
                adicionar_vertice_e_arestas(vertice.esquerda, vertice, 'esquerda')
                adicionar_vertice_e_arestas(vertice.direita, vertice, 'direita')
        adicionar_vertice_e_arestas(self.ponto_inicial)
        return G

class Estrutura_Interface:
    def __init__(self, janela_principal):
        self.janela_principal = janela_principal
        janela_principal.title("🌌 Arvore Binaria de Busca (ABB) - CustomTkinter")
        janela_principal.geometry("1200x800")
        set_appearance_mode("Dark") 
        set_default_color_theme("blue")
        self.apb = EstruturaBuscaBinaria()
        self.funcao_selecionada = StringVar(value="P")
        self.status_operacao = StringVar()
        entrada_padrao = "15, 6, 18, 3, 7, 17, 20, 2, 4, 13, 9, 10, 8, 16, 19, 21, 1, 5, 12, 14, 22, 0, 25, 23, 24"

        principal_quadro = CTkFrame(janela_principal, fg_color="transparent")
        principal_quadro.pack(fill=BOTH, expand=True, padx=20, pady=20)
        
        configuracao_quadro = CTkFrame(principal_quadro, corner_radius=10)
        configuracao_quadro.grid(row=0, column=0, sticky="n", padx=10, pady=10)
        CTkLabel(configuracao_quadro, text="🔮 Configuracao Inicial", font=CTkFont(weight="bold")).pack(pady=(10, 5), padx=10)

        funcoes_quadro = CTkFrame(principal_quadro, corner_radius=10)
        funcoes_quadro.grid(row=1, column=0, sticky="n", padx=10, pady=10)
        CTkLabel(funcoes_quadro, text="🚀 Operacoes", font=CTkFont(weight="bold")).pack(pady=(10, 5), padx=10)

        visualizacao_quadro = CTkFrame(principal_quadro, corner_radius=10)
        visualizacao_quadro.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=10, pady=10)
        CTkLabel(visualizacao_quadro, text="🔭 Representacao Grafica da Arvore", font=CTkFont(weight="bold")).pack(pady=(10, 5))

        principal_quadro.grid_columnconfigure(1, weight=1)
        principal_quadro.grid_rowconfigure(0, weight=1)

        CTkLabel(configuracao_quadro, text="Valores:").pack(anchor="w", padx=10)
        self.campo_entrada = CTkEntry(configuracao_quadro, width=300)
        self.campo_entrada.insert(0, entrada_padrao)
        self.campo_entrada.pack(pady=5, padx=10)

        self.botao_compor = CTkButton(configuracao_quadro, text="Compor/Reorganizar Estrutura", command=self.compor_estrutura, fg_color="#8A2BE2")
        self.botao_compor.pack(pady=10, padx=10, fill='x')

        self.rotulo_status = CTkLabel(configuracao_quadro, textvariable=self.status_operacao, text_color="green")
        self.rotulo_status.pack(pady=5, padx=10)

        CTkLabel(funcoes_quadro, text="Escolha o procedimento:").pack(anchor="w", padx=10)
        CTkRadioButton(funcoes_quadro, text="Pesquisar (P)", variable=self.funcao_selecionada, value="P").pack(anchor="w", padx=10)
        CTkRadioButton(funcoes_quadro, text="Adicionar (A)", variable=self.funcao_selecionada, value="A").pack(anchor="w", padx=10)
        CTkRadioButton(funcoes_quadro, text="Eliminar (E) -> Refaz/Equilibra", variable=self.funcao_selecionada, value="E").pack(anchor="w", padx=10)
        
        CTkLabel(funcoes_quadro, text="Valor Numerico:").pack(anchor="w", padx=10, pady=(10, 0))
        self.entrada_operacao_valor = CTkEntry(funcoes_quadro, width=100)
        self.entrada_operacao_valor.pack(pady=5, padx=10, anchor="w")
        
        self.botao_executar = CTkButton(funcoes_quadro, text="Executar Procedimento", command=self.executar_procedimento, fg_color="#DA70D6")
        self.botao_executar.pack(pady=10, padx=10, fill='x')

        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=visualizacao_quadro)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        self.compor_estrutura() 

    def compor_estrutura(self):
        texto_entrada = self.campo_entrada.get().replace(' ', ',')
        partes = [p.strip() for p in texto_entrada.split(',') if p.strip()]
        
        try:
            valores_iniciais = sorted(list(set([int(p) for p in partes])))
            
            self.apb = EstruturaBuscaBinaria()
            self.apb.ponto_inicial = self.apb._compor_estrutura_balanceada_recursiva(valores_iniciais)
            
            self.status_operacao.set(f"✅ Arvore construida com {len(self.apb.obter_elementos_em_ordem())} elementos.")
            self.rotulo_status.configure(text_color="green")
            self.apresentar_estrutura()
            
        except ValueError as e:
            self.status_operacao.set(f"❌ Erro: Valor invalido.")
            self.rotulo_status.configure(text_color="red")
            messagebox.showerror("Erro na Insercao", "Apenas numeros inteiros separados por virgula são permitidos.")
            self.apb = EstruturaBuscaBinaria()
            self.apresentar_estrutura()

    def executar_procedimento(self):
        tipo_operacao = self.funcao_selecionada.get()
        texto_valor_operacao = self.entrada_operacao_valor.get()
        
        if not texto_valor_operacao:
            self.status_operacao.set("⚠️ Insira um valor para o procedimento.")
            self.rotulo_status.configure(text_color="orange"); return

        try: valor = int(texto_valor_operacao)
        except ValueError:
            self.status_operacao.set("❌ Erro: O valor deve ser um numero inteiro.")
            self.rotulo_status.configure(text_color="red"); return

        mensagem = ""; estrutura_modificada = False
        
        if tipo_operacao == 'A':
            if self.apb.buscar_dado(valor):
                mensagem = f"⚠️ Valor {valor} ja esta presente."
            else:
                self.apb.adicionar_dado(valor)
                self.apb.ponto_inicial = self.apb._compor_estrutura_balanceada_recursiva(self.apb.obter_elementos_em_ordem())
                mensagem = f"✅ Valor {valor} adicionado e arranjo equilibrado."; estrutura_modificada = True
            
        elif tipo_operacao == 'E':
            sucesso, msg = self.apb.eliminar(valor)
            mensagem = msg; estrutura_modificada = sucesso
            
        elif tipo_operacao == 'P':
            mensagem = f"✅ Valor {valor} esta no arranjo." if self.apb.buscar_dado(valor) else f"❌ Valor {valor} nao esta no arranjo."
        
        self.status_operacao.set(mensagem)
        if mensagem.startswith("✅"): self.rotulo_status.configure(text_color="green")
        elif mensagem.startswith("❌"): self.rotulo_status.configure(text_color="red")
        elif mensagem.startswith("⚠️"): self.rotulo_status.configure(text_color="orange")
        else: self.rotulo_status.configure(text_color="white")

        if estrutura_modificada or tipo_operacao == 'P':
            self.apresentar_estrutura(valor if tipo_operacao == 'P' else None)
            
    def apresentar_estrutura(self, valor_procurado=None):
        G = self.apb.gerar_grafo()
        self.figure.clear(); ax = self.figure.add_subplot(111)
        
        if G.number_of_nodes() == 0:
            ax.text(0.5, 0.5, "Árvore Vazia", ha='center', va='center', fontsize=20, color='white')
            ax.set_xticks([]); ax.set_yticks([]); self.canvas.draw(); return
            
        pos = self._calcular_posicoes_arvore(G, self.apb.ponto_inicial.dado)
        node_colors = ['#00BFFF' if node != valor_procurado else '#FFD700' for node in G.nodes()]
        
        nx.draw(G, pos, ax=ax, with_labels=True, node_size=2000, node_color=node_colors, 
                font_size=12, font_weight='bold', font_color='black', edge_color='#A9A9A9', arrows=False)
        
        ax.set_title(f"ABB Balanceada - {G.number_of_nodes()} Nós", color='white')
        self.canvas.draw()
        
    def _calcular_posicoes_arvore(self, G, raiz, largura=1.0, altura=1.0, x=0, y=0, pos=None, nivel=1):
        if pos is None: pos = {raiz: (x, y)}
        vizinhos = list(G.successors(raiz))
        
        if vizinhos:
            largura_total = largura; largura_segmento = largura_total / len(vizinhos)
            x_atual = x - (largura_total / 2) + (largura_segmento / 2)
            
            for vizinho in vizinhos:
                relacao = G.get_edge_data(raiz, vizinho)['relacao']
                
                if relacao == 'esquerda': x_novo = x_atual - largura_segmento/4
                else: x_novo = x_atual + largura_segmento/4

                y_novo = y - altura
                pos[vizinho] = (x_novo, y_novo)
                
                self._calcular_posicoes_arvore(G, vizinho, largura_segmento, altura, x_novo, y_novo, pos, nivel + 1)
                x_atual += largura_segmento
        return pos


if __name__ == "__main__":
    janela_mestra = CTk()
    aplicacao = Estrutura_Interface(janela_mestra)
    janela_mestra.mainloop()
