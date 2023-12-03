import tkinter as tk
from tkinter import simpledialog, messagebox
from source.Bot import bot_expressao, bot_arquivo

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de Expressões")

        self.expression_button = tk.Button(master, text="Expressão", command=self.execute_expression)
        self.expression_button.pack()

        self.result_text = tk.Text(master, height=10, width=40)
        self.result_text.pack()

    def execute_expression(self):
        expression = self.get_user_input("Digite a expressão/variável:")
        try:
            result = bot_expressao({}, expression, from_gui=True)
            self.show_result(result)
        except Exception as e:
            self.show_result(str(e))


    def get_user_input(self, prompt):
        return simpledialog.askstring("Entrada", prompt)

    def show_result(self, result):
        self.result_text.insert(tk.END, str(result) + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
