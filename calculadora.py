import tkinter as tk
from tkinter import messagebox
from math import sqrt


class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x450')
        self.resizable(0, 0)
        self.title('Calculadora')
        self.iconbitmap('calculadora.ico')
        self.expresion = ''
        self.entrada_texto = tk.StringVar()
        self._creacion_componentes()

    def _creacion_componentes(self):
        entrada_frame = tk.Frame(self, height=50, bg='grey')
        entrada_frame.pack(side=tk.TOP, fill='x')
        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'),
                           textvariable=self.entrada_texto, justify=tk.RIGHT)
        entrada.pack(fill='both', ipady=10)

        botones_frame = tk.Frame(self, bg='grey')
        botones_frame.pack(fill='both', expand=True)

        # Configurar filas y columnas para que se expandan
        for i in range(5):  # hay 5 filas
            botones_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):  # hay 4 columnas
            botones_frame.grid_columnconfigure(j, weight=1)

        botones = [
            # (texto, fila, columna, rowspan, colspan, función que se ejecuta)
            ('C', 0, 0, 1, 3, self._evento_limpiar),
            ('/', 0, 3, 1, 1, lambda: self._evento_click('/')),
            ('7', 1, 0, 1, 1, lambda: self._evento_click('7')),
            ('8', 1, 1, 1, 1, lambda: self._evento_click('8')),
            ('9', 1, 2, 1, 1, lambda: self._evento_click('9')),
            ('*', 1, 3, 1, 1, lambda: self._evento_click('*')),
            ('4', 2, 0, 1, 1, lambda: self._evento_click('4')),
            ('5', 2, 1, 1, 1, lambda: self._evento_click('5')),
            ('6', 2, 2, 1, 1, lambda: self._evento_click('6')),
            ('-', 2, 3, 1, 1, lambda: self._evento_click('-')),
            ('1', 3, 0, 1, 1, lambda: self._evento_click('1')),
            ('2', 3, 1, 1, 1, lambda: self._evento_click('2')),
            ('3', 3, 2, 1, 1, lambda: self._evento_click('3')),
            ('+', 3, 3, 1, 1, lambda: self._evento_click('+')),
            ('0', 4, 0, 1, 2, lambda: self._evento_click('0')),
            ('.', 4, 2, 1, 1, lambda: self._evento_click('.')),
            ('=', 4, 3, 1, 1, self._evento_evaluar),
        ]

        # Crear los botones uno a uno
        # (texto, fila, columna, rowspan, colspan, función que se ejecuta)
        for texto, fila, columna, rowspan, colspan, comando in botones:
            boton = tk.Button(botones_frame, text=texto, bd=0.5,
                              bg='#eee' if texto in 'C/*-+=' else '#fff',
                              cursor='hand2', command=comando)

            # coloca el boton en su sitio
            boton.grid(row=fila, column=columna,
                       rowspan=rowspan, columnspan=colspan,
                       padx=1, pady=1, sticky='nsew')

    def _evento_evaluar(self):
        try:
            if self.expresion:
                resultado = str(eval(self.expresion))  # eval() convierte el texto en una operación real
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror('Error', f'Ocurrió un error: {e}')
            self.entrada_texto.set('')
        finally:
            self.expresion = ''

    def _evento_limpiar(self):
        self.expresion = ''
        self.entrada_texto.set('')

    def _evento_click(self, elemento):
        self.expresion += elemento
        self.entrada_texto.set(self.expresion)


if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()
