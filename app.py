import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")

        self.display = tk.Entry(root, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

        self.root.bind("<Key>", self.press_key)

    def create_buttons(self):
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
            ("C", 5, 0), ("√", 5, 1), ("^", 5, 2), ("^2", 5, 3),
            ("sin", 6, 0), ("cos", 6, 1), ("tan", 6, 2), ("log", 6, 3),
            ("exp", 7, 0), ("!", 7, 1)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self.root, text=text, padx=20, pady=10, command=lambda t=text: self.display.insert(tk.END, t))
            button.grid(row=row, column=column, padx=5, pady=5)
            if text == "=":
                button.config(command=self.calculate)
            elif text == "C":
                button.config(command=self.clear)
            elif text == "√":
                button.config(command=self.square_root)
            elif text == "^":
                button.config(command=self.power)
            elif text == "sin":
                button.config(command=self.sine)
            elif text == "cos":
                button.config(command=self.cosine)
            elif text == "tan":
                button.config(command=self.tangent)
            elif text == "log":
                button.config(command=self.logarithm)
            elif text == "exp":
                button.config(command=self.exponential)
            elif text == "!":
                button.config(command=self.factorial)

    def press_key(self, event):
        if event.keysym in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            self.display.insert(tk.END, event.keysym)
        elif event.keysym == "BackSpace":
            self.display.delete(len(self.display.get())-1, tk.END)
        elif event.keysym == "Return":
            self.calculate()
        elif event.keysym == "period":
            self.display.insert(tk.END, ".")
        elif event.keysym == "plus":
            self.display.insert(tk.END, "+")
        elif event.keysym == "minus":
            self.display.insert(tk.END, "-")
        elif event.keysym == "asterisk":
            self.display.insert(tk.END, "*")
        elif event.keysym == "slash":
            self.display.insert(tk.END, "/")
        elif event.keysym == "Escape":
            self.clear()

    def calculate(self):
        expression = self.display.get()
        try:
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

    def clear(self):
        self.display.delete(0, tk.END)

    def square_root(self):
        value = self.display.get()
        try:
            result = math.sqrt(float(value))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

    def power(self):
        base = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, base+"**")

    def sine(self):
        value = self.display.get()
        try:
            result = math.sin(math.radians(float(value)))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

    def cosine(self):
        value = self.display.get()
        try:
            result = math.cos(math.radians(float(value)))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

    def tangent(self):
        value = self.display.get()
        try:
            result = math.tan(math.radians(float(value)))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

    def logarithm(self):
        value = self.display.get()
        try:
            result = math.log10(float(value))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

    def exponential(self):
        value = self.display.get()
        try:
            result = math.exp(float(value))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

    def factorial(self):
        value = self.display.get()
        try:
            result = math.factorial(int(value))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

# Cria a janela principal
root = tk.Tk()
app = Calculator(root)
root.mainloop()
