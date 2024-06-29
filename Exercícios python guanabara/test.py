import tkinter as tk
from tkinter import messagebox
import psycopg2

class CadastroUsuario:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Usuário")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.label_nome = tk.Label(self.frame, text="Nome:")
        self.label_nome.grid(row=0, column=0, padx=5, pady=5)

        self.entry_nome = tk.Entry(self.frame)
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        self.label_email = tk.Label(self.frame, text="Email:")
        self.label_email.grid(row=1, column=0, padx=5, pady=5)

        self.entry_email = tk.Entry(self.frame)
        self.entry_email.grid(row=1, column=1, padx=5, pady=5)

        self.btn_cadastrar = tk.Button(self.frame, text="Cadastrar", command=self.cadastrar_usuario)
        self.btn_cadastrar.grid(row=2, columnspan=2, padx=5, pady=5)

    def cadastrar_usuario(self):
        nome = self.entry_nome.get()
        email = self.entry_email.get()

        try:
            # Conexão com o banco de dados PostgreSQL
            connection = psycopg2.connect(
                host="localhost",
                database="seu_banco_de_dados",
                user="seu_usuario",
                password="sua_senha"
            )

            cursor = connection.cursor()

            # Inserção dos dados do usuário no banco de dados
            cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome, email))
            connection.commit()

            messagebox.showinfo("Cadastro Efetuado", "Usuário cadastrado com sucesso!")

            # Fechar a conexão com o banco de dados
            cursor.close()
            connection.close()

        except (Exception, psycopg2.Error) as error:
            messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {error}")

        self.limpar_campos()

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)


class SistemaNotas:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Registro de Notas")

        # Adicionei a conexão ao banco de dados aqui para ser utilizada em ambas as classes
        self.connection = psycopg2.connect(
            host="localhost",
            database="seu_banco_de_dados",
            user="seu_usuario",
            password="sua_senha"
        )

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        self.label_aluno = tk.Label(self.frame, text="Nome do Aluno:")
        self.label_aluno.grid(row=0, column=0, padx=5, pady=5)

        self.entry_aluno = tk.Entry(self.frame)
        self.entry_aluno.grid(row=0, column=1, padx=5, pady=5)

        self.label_nota = tk.Label(self.frame, text="Nota:")
        self.label_nota.grid(row=1, column=0, padx=5, pady=5)

        self.entry_nota = tk.Entry(self.frame)
        self.entry_nota.grid(row=1, column=1, padx=5, pady=5)

        self.btn_registrar = tk.Button(self.frame, text="Registrar Nota", command=self.registrar_nota)
        self.btn_registrar.grid(row=2, columnspan=2, padx=5, pady=5)

    def registrar_nota(self):
        aluno = self.entry_aluno.get()
        nota = self.entry_nota.get()

        try:
            cursor = self.connection.cursor()

            # Aqui você pode adicionar lógica para salvar a nota no banco de dados
            # Neste exemplo, apenas exibimos uma mensagem com os detalhes da nota
            messagebox.showinfo("Nota Registrada", f"Nota de {aluno} registrada: {nota}")

            cursor.close()

        except (Exception, psycopg2.Error) as error:
            messagebox.showerror("Erro", f"Erro ao registrar nota: {error}")

        self.limpar_campos()

    def limpar_campos(self):
        self.entry_aluno.delete(0, tk.END)
        self.entry_nota.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()

    # Cria a tabela "usuarios" no banco de dados se ela não existir
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="seu_banco_de_dados",
            user="seu_usuario",
            password="sua_senha"
        )

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL
            )
        """)

        connection.commit()

        cursor.close()
        connection.close()

    except (Exception, psycopg2.Error) as error:
        messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {error}")

    # Executa a aplicação
    app = CadastroUsuario(root)
    root.mainloop()

