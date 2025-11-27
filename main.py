import tkinter as tk
from tkinter import messagebox
from customtkinter import *

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
        if vertice is None:
            return Vertice(dado)
        if dado < vertice.dado:
            vertice.esquerda = self._adicionar_recursivo(vertice.esquerda, dado)
        elif dado > vertice.dado:
            vertice.direita = self._adicionar_recursivo(vertice.direita, dado)
        return vertice

    def buscar_dado(self, dado):
        return self._buscar_recursivo(self.ponto_inicial, dado)

    def _buscar_recursivo(self, vertice, dado):
        if vertice is None or vertice.dado == dado:
            return vertice is not None
        if dado < vertice.dado:
            return self._buscar_recursivo(vertice.esquerda, dado)
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
    
    # --- NOVO METODO PARA CONSTRUCAO BALANCEADA ---
    def _compor_estrutura_balanceada_recursiva(self, elementos):
        if not elementos:
            return None
        
        meio = len(elementos) // 2
        vertice_inicio = Vertice(elementos[meio])
        
        vertice_inicio.esquerda = self._compor_estrutura_balanceada_recursiva(elementos[:meio])
        vertice_inicio.direita = self._compor_estrutura_balanceada_recursiva(elementos[meio + 1:])
        
        return vertice_inicio
    # ------------------------------------------------

    def eliminar(self, dado):
        if not self.buscar_dado(dado):
            return False, f"❌ Dado {dado} indisponivel para eliminacao."
            
        lista_ordenada = self.obter_elementos_em_ordem()
        lista_ordenada.remove(dado)
        
        # 1. Destroi o ponto de inicio (opcional, mas limpa a estrutura)
        self.ponto_inicial = None
        
        # 2. Reconstroi usando o algoritmo de balanceamento
        self.ponto_inicial = self._compor_estrutura_balanceada_recursiva(lista_ordenada)
            
        return True, f"✅ Dado {dado} eliminado e o arranjo foi refeito/equilibrado."
    
    def apresentar_estrutura_em_texto(self):
        if not self.ponto_inicial:
            return "Arranjo de dados vazio."
        linhas, _, _, _ = self._auxilio_apresentacao(self.ponto_inicial)
        texto_estrutura = "\n".join(linhas)
        return texto_estrutura

    def _auxilio_apresentacao(self, vertice):
        if vertice.direita is None and vertice.esquerda is None:
            linha = str(vertice.dado)
            largura = len(linha)
            altura = 1
            return [linha], largura, altura, largura // 2

        if vertice.direita is None:
            linhas, n, p, x = self._auxilio_apresentacao(vertice.esquerda)
            s = str(vertice.dado)
            largura = len(s)
            linha_primeira = (x + 1) * ' ' + (n - x - 1) * '_' + s
            linha_segunda = x * ' ' + '/' + (n - x - 1 + largura) * ' '
            linhas_deslocadas = [linha + largura * ' ' for linha in linhas]
            return [linha_primeira, linha_segunda] + linhas_deslocadas, n + largura, p + 2, n + largura // 2

        if vertice.esquerda is None:
            linhas, n, p, x = self._auxilio_apresentacao(vertice.direita)
            s = str(vertice.dado)
            largura = len(s)
            linha_primeira = s + x * '_' + (n - x) * ' '
            linha_segunda = (largura + x) * ' ' + '\\' + (n - x - 1) * ' '
            linhas_deslocadas = [largura * ' ' + linha for linha in linhas]
            return [linha_primeira, linha_segunda] + linhas_deslocadas, n + largura, p + 2, largura // 2

        esquerda_blocos, n, p, x = self._auxilio_apresentacao(vertice.esquerda)
        direita_blocos, m, q, y = self._auxilio_apresentacao(vertice.direita)
        s = str(vertice.dado)
        largura = len(s)
        
        linha_primeira = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        linha_segunda = x * ' ' + '/' + (n - x - 1 + largura + y) * ' ' + '\\' + (m - y - 1) * ' '
        
        if p < q:
            esquerda_blocos += [n * ' '] * (q - p)
        elif q < p:
            direita_blocos += [m * ' '] * (p - q)
            
        linhas = [linha_primeira, linha_segunda] + [a + largura * ' ' + b for a, b in zip(esquerda_blocos, direita_blocos)]
        return linhas, n + m + largura, max(p, q) + 2, n + largura // 2

class Estrutura_Interface:
    def __init__(self, janela_principal):
        self.janela_principal = janela_principal
        janela_principal.title("🌌 Arvore Binaria de Busca (ABB) - CustomTkinter")
        janela_principal.geometry("1000x750")

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
        funcoes_quadro.grid(row=0, column=1, sticky="n", padx=10, pady=10)
        CTkLabel(funcoes_quadro, text="🚀 Operacoes", font=CTkFont(weight="bold")).pack(pady=(10, 5), padx=10)

        visualizacao_quadro = CTkFrame(principal_quadro, corner_radius=10)
        visualizacao_quadro.grid(row=0, column=2, rowspan=2, sticky="nsew", padx=10, pady=10)
        CTkLabel(visualizacao_quadro, text="🔭 Representacao da Arvore", font=CTkFont(weight="bold")).pack(pady=(10, 5))

        principal_quadro.grid_columnconfigure(2, weight=1)
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

        self.expositor_estrutura = CTkTextbox(visualizacao_quadro, wrap="none", height=20, width=50, font=("Courier", 12))
        self.expositor_estrutura.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        self.compor_estrutura() 

    def processar_entrada(self, texto_entrada):
        texto_entrada = texto_entrada.replace(' ', ',')
        partes = [p.strip() for p in texto_entrada.split(',') if p.strip()]
        
        numeros = []
        for parte in partes:
            try:
                numeros.append(int(parte))
            except ValueError:
                raise ValueError(f"O item '{parte}' nao e um valor inteiro valido.")
        return numeros

    def compor_estrutura(self):
        texto_entrada = self.campo_entrada.get()
        try:
            valores_iniciais = self.processar_entrada(texto_entrada)
            
            self.apb = EstruturaBuscaBinaria()
            # Utilizar o metodo de equilibrio para a construcao inicial
            valores_iniciais.sort()
            self.apb.ponto_inicial = self.apb._compor_estrutura_balanceada_recursiva(valores_iniciais)
            
            self.status_operacao.set(f"✅ Arvore construida com {len(self.apb.obter_elementos_em_ordem())} vertices/Elementos.")
            self.rotulo_status.configure(text_color="green")
            self.apresentar_estrutura()
            
        except ValueError as e:
            self.status_operacao.set(f"❌ Erro na Insercao.")
            self.rotulo_status.configure(text_color="red")
            messagebox.showerror("Erro na Insercao", str(e))
            self.apb = EstruturaBuscaBinaria()
            self.apresentar_estrutura()

    def executar_procedimento(self):
        tipo_operacao = self.funcao_selecionada.get()
        texto_valor_operacao = self.entrada_operacao_valor.get()
        
        if not texto_valor_operacao:
            self.status_operacao.set("⚠️ Insira um valor para o procedimento.")
            self.rotulo_status.configure(text_color="orange")
            return

        try:
            valor = int(texto_valor_operacao)
        except ValueError:
            self.status_operacao.set("❌ Erro: O valor deve ser um numero inteiro.")
            self.rotulo_status.configure(text_color="red")
            return

        mensagem = ""
        estrutura_modificada = False
        
        if tipo_operacao == 'A':
            if self.apb.buscar_dado(valor):
                mensagem = f"⚠️ Valor {valor} ja se encontra presente. Nada foi alterado."
                self.rotulo_status.configure(text_color="orange")
            else:
                self.apb.adicionar_dado(valor)
                # Recria a arvore de forma equilibrada apos a inclusao (para manter o balanceamento)
                lista_ordenada = self.apb.obter_elementos_em_ordem()
                self.apb.ponto_inicial = self.apb._compor_estrutura_balanceada_recursiva(lista_ordenada)
                
                mensagem = f"✅ Valor {valor} adicionado e arranjo equilibrado."
                estrutura_modificada = True
            
        elif tipo_operacao == 'E':
            sucesso, msg = self.apb.eliminar(valor)
            mensagem = msg
            estrutura_modificada = sucesso
            
        elif tipo_operacao == 'P':
            if self.apb.buscar_dado(valor):
                mensagem = f"✅ Valor {valor} esta no arranjo."
            else:
                mensagem = f"❌ Valor {valor} nao esta no arranjo."
        
        if tipo_operacao != 'A' or not mensagem.startswith("⚠️"):
            self.status_operacao.set(mensagem)
            if mensagem.startswith("✅"):
                self.rotulo_status.configure(text_color="green")
            elif mensagem.startswith("❌"):
                self.rotulo_status.configure(text_color="red")
            elif mensagem.startswith("⚠️"):
                self.rotulo_status.configure(text_color="orange")
            else:
                self.rotulo_status.configure(text_color="white")

        if estrutura_modificada:
            self.apresentar_estrutura()
            
    def apresentar_estrutura(self):
        texto_estrutura = self.apb.apresentar_estrutura_em_texto()
        self.expositor_estrutura.delete('1.0', END)
        
        quantidade_valores = len(self.apb.obter_elementos_em_ordem())
        self.expositor_estrutura.insert(END, f"Total de valores: {quantidade_valores}\n\n")
        self.expositor_estrutura.insert(END, texto_estrutura)

if __name__ == "__main__":
    janela_mestra = CTk()
    aplicacao = Estrutura_Interface(janela_mestra)
    janela_mestra.mainloop()