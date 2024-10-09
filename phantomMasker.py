import os
import tkinter as tk
from tkinter import filedialog, messagebox


# Função para aplicar o caractere Unicode 202E e inverter a extensão
def apply_unicode_rlo(file_name, fake_extension):
    rlo_char = "\u202E"
    reversed_extension = fake_extension[::-1]
    new_name = file_name + rlo_char + reversed_extension + ".exe"
    return new_name


# Função para renomear o executável
def rename_executable(exe_path, fake_extension, lang):
    valid_extensions = ['.png', '.jpeg', '.pdf']
    if fake_extension not in valid_extensions:
        if lang == "pt":
            messagebox.showerror("Erro", f"Extensão inválida. Escolha entre {valid_extensions}")
        else:
            messagebox.showerror("Error", f"Invalid extension. Choose from {valid_extensions}")
        return

    base_name = os.path.basename(exe_path)
    file_name, _ = os.path.splitext(base_name)

    obfuscated_name = apply_unicode_rlo(file_name, fake_extension)
    new_path = os.path.join(os.path.dirname(exe_path), obfuscated_name)

    try:
        os.rename(exe_path, new_path)
        if lang == "pt":
            messagebox.showinfo("Sucesso", f"Arquivo renomeado para: {new_path}")
        else:
            messagebox.showinfo("Success", f"File renamed to: {new_path}")
    except Exception as e:
        if lang == "pt":
            messagebox.showerror("Erro", f"Erro ao renomear o arquivo: {e}")
        else:
            messagebox.showerror("Error", f"Error renaming the file: {e}")


# Função chamada ao clicar no botão "Escolher Arquivo"
def select_file(lang):
    if lang == "pt":
        file_path = filedialog.askopenfilename(title="Selecione o arquivo", filetypes=[("Executável", "*.exe")])
    else:
        file_path = filedialog.askopenfilename(title="Select the file", filetypes=[("Executable", "*.exe")])

    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)


# Função chamada ao clicar no botão "Renomear"
def rename_file(lang):
    exe_file = file_entry.get()
    fake_extension = extension_var.get()
    if not exe_file:
        if lang == "pt":
            messagebox.showwarning("Aviso", "Por favor, escolha um arquivo.")
        else:
            messagebox.showwarning("Warning", "Please choose a file.")
        return
    rename_executable(exe_file, fake_extension, lang)


# Função para mudar o idioma da interface
def change_language(lang):
    if lang == "pt":
        root.title("PhantomMasker - Ocultador de Extensões de Executáveis")
        title_label.config(text="PhantomMasker")
        file_button.config(text="Escolher Arquivo")
        extensions_label.config(text="Escolha a extensão falsa:")
        rename_button.config(text="Renomear")
        exit_button.config(text="Sair")
        lang_menu.entryconfig(0, label="Inglês")
        lang_menu.entryconfig(1, label="Português")
    else:
        root.title("PhantomMasker - File Extension Hider")
        title_label.config(text="PhantomMasker")
        file_button.config(text="Select File")
        extensions_label.config(text="Choose fake extension:")
        rename_button.config(text="Rename")
        exit_button.config(text="Exit")
        lang_menu.entryconfig(0, label="English")
        lang_menu.entryconfig(1, label="Portuguese")


# Função para sair do programa
def exit_program():
    root.destroy()


# Criação da janela principal
root = tk.Tk()
root.title("PhantomMasker - File Extension Hider")

# Definir tamanho da janela
root.geometry("420x280")
root.resizable(False, False)

# Configurações de estilo (cores e fonte)
root.configure(bg="#1e1e1e")
title_font = ("Helvetica", 16, "bold")
label_font = ("Helvetica", 12)

# Título
title_label = tk.Label(root, text="PhantomMasker", font=title_font, fg="#7289DA", bg="#1e1e1e")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Entrada de texto para o caminho do arquivo
file_entry = tk.Entry(root, width=45, font=("Arial", 10))
file_entry.grid(row=1, column=1, padx=10, pady=10)

# Botão para selecionar o arquivo .exe
file_button = tk.Button(root, text="Select File", command=lambda: select_file(lang_var.get()), bg="#7289DA", fg="white")
file_button.grid(row=1, column=0, padx=10, pady=10)

# Rótulo para escolha de extensão
extensions_label = tk.Label(root, text="Choose fake extension:", font=label_font, fg="white", bg="#1e1e1e")
extensions_label.grid(row=2, column=0, padx=10, pady=10)

# Menu de seleção de extensão
extension_var = tk.StringVar(value=".png")
extensions_menu = tk.OptionMenu(root, extension_var, ".png", ".jpeg", ".pdf")
extensions_menu.config(bg="#7289DA", fg="white")
extensions_menu.grid(row=2, column=1, padx=10, pady=10)

# Botão para renomear o arquivo
rename_button = tk.Button(root, text="Rename", command=lambda: rename_file(lang_var.get()), bg="#43B581", fg="white")
rename_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Botão para sair do programa
exit_button = tk.Button(root, text="Exit", command=exit_program, bg="#F04747", fg="white")
exit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Menu para escolha de idioma
menubar = tk.Menu(root)
lang_menu = tk.Menu(menubar, tearoff=0)
lang_menu.add_command(label="English", command=lambda: change_language("en"))
lang_menu.add_command(label="Portuguese", command=lambda: change_language("pt"))
menubar.add_cascade(label="Language", menu=lang_menu)
root.config(menu=menubar)

# Variável para armazenar o idioma atual
lang_var = tk.StringVar(value="en")

# Executa a aplicação
root.mainloop()
