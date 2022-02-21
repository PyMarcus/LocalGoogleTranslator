"""
1) Frame de fundo
2) combobox para selecao de linguagem de entrada
3) combobox para selecao de linguagem de saida
4) caixa de entrada
5) caixa de saida
6) botao de traduzir
"""
from tkinter import ttk, Tk, Text, Button
#from multiprocessing import Process
#from googletrans import Translator
#rom google_trans_new import google_translator
from ttkbootstrap import Style

import translators as ts



def translate():
    """Traduz a frase passada no container de entrada"""
    tr = ts
    text = textbox.get('1.0', 'end')  # pega entrada da linha 1 coluna zero ao final
    src = str(select_box.get()).replace('Português', 'pt').replace('English', 'en').replace('Deutch', 'de').replace('Turkish', 'tr').replace('Español', 'es')
    dest = str(select_box1.get()).replace('Português', 'pt').replace('English', 'en').replace('Deutch', 'de').replace('Turkish', 'tr').replace('Español', 'es')
    print(src, dest)
    translat = ts.google(query_text=text, from_language='auto', to_language=dest.replace(' ', ''))
    # permissões para digitar ou nao
    #text_box.config(state="disable")
    text_box.config(state="normal")
    text_box.delete('1.0', 'end') # deleta o que tiver
    text_box.insert('1.0', translat) # onde escrever e o que
    text_box.config(state="disable") # volta ao bloqueio


"""Gera a interface"""
#window = Tk()  # widget master, principal.
style = Style('superhero')
window = style.master
languages: list = ['Português', "Español", "English", "Deutch"]

"""Constroí widgets para entrada de texto"""
container = ttk.Frame()  # container para agrupar e empacotar itens

# indicativo: rotulo
label = ttk.Label(container, text="Traduzir: ", font=("Monospace", 15))  # mini rotulo para indicar o que traduzir
label.grid(row=0, column=0, padx=10, pady=10) # coloca na posicao 0, 0 do container

# caixa de seleção
select_box = ttk.Combobox(container, values=languages) # caixa de seleção de linguagens
select_box.set(" Idiomas:")
select_box.grid(row=0, column=1, padx=10, pady=10)  # coloca ao lado do label

# caixa de texto
textbox = Text(width=50, height=10, font=("Monospace", 10))

# empacotamento
container.pack(fill="both", expand="yes")
textbox.pack(padx=10, pady=10, fill="both", expand="yes")


"""Constroi widget para saída de texto"""
container1 = ttk.Frame()
# rotulo
label2 = ttk.Label(container1, text="Tradução: ", font=("Monospace", 15))
label2.grid(row=0, column=0, padx=10, pady=10)  # coloca na posicao 0, 0 do container

# caixa de seleção
select_box1 = ttk.Combobox(container1, values=languages)  # caixa de seleção de linguagens
select_box1.set(" Idiomas:")
select_box1.grid(row=0, column=1, padx=10, pady=10)  # coloca ao lado do label

# caixa de texto
text_box = Text(width=50, height=10, font=("Monospace", 10), state="disable")  # caixa de texto para entrada de digitações


# empacotamento
container1.pack(fill="both", expand="yes")  # redimenciona com o container master
text_box.pack(padx=10, pady=10, fill="both", expand="yes")

button = Button(text="Traduzir", font=("Monospace", 13), command=translate)
button.bind('<Return>', translate)  # permite apertar enter para executar
#button.grid(row=3, column=50)
button.pack(padx=10, pady=20)



# janela principal main-content
window.title("TRADUTOR")
window.mainloop()  # loop para permanência da janela, até fechar

