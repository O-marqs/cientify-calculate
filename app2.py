import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Científica")

        self.display = tk.Entry(root, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        self.create_buttons()

        self.root.bind("<Key>", self.press_key)

    def create_buttons(self):
        buttons = [
            ("7", 1, 0, 1), ("8", 1, 1, 1), ("9", 1, 2, 1), ("/", 1, 3, 1), ("sin", 1, 4, 1), ("asin", 1, 5, 1),
            ("4", 2, 0, 1), ("5", 2, 1, 1), ("6", 2, 2, 1), ("*", 2, 3, 1), ("cos", 2, 4, 1), ("acos", 2, 5, 1),
            ("1", 3, 0, 1), ("2", 3, 1, 1), ("3", 3, 2, 1), ("-", 3, 3, 1), ("tan", 3, 4, 1), ("atan", 3, 5, 1),
            ("0", 4, 1, 1), (".", 4, 0, 1), ("=", 4, 2, 1), ("+", 4, 3, 1), ("exp", 4, 4, 1), ("log", 4, 5, 1),
            ("(", 5, 0, 1), (")", 5, 1, 1), ("√", 5, 2, 1), ("^", 5, 3, 1), ("sinh", 5, 4, 1), ("asinh", 5, 5, 1),
            ("π", 6, 0, 1), ("e", 6, 1, 1), ("^2", 6, 2, 1), ("1/x", 6, 3, 1), ("cosh", 6, 4, 1), ("acosh", 6, 5, 1),
            ("C", 7, 0, 2), ("CE", 7, 2, 2)
        ]

        for (text, row, column, columnspan) in buttons:
            button = tk.Button(self.root, text=text, padx=20, pady=10, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)
            if text == "=":
                button.config(command=self.calculate)
            elif text == "C":
                button.config(command=self.clear_all)
            elif text == "CE":
                button.config(command=self.clear)
            elif text in ["sin", "cos", "tan", "asin", "acos", "atan", "sinh", "cosh", "asinh", "acosh"]:
                button.config(command=lambda t=text: self.trigonometric_function(t))
            elif text == "log":
                button.config(command=self.logarithm)
            elif text == "^":
                button.config(command=self.power)
            elif text == "√":
                button.config(command=self.square_root)
            elif text == "exp":
                button.config(command=self.exponential)
            elif text == "π":
                button.config(command=self.pi)
            elif text == "e":
                button.config(command=self.e)
            elif text == "^2":
                button.config(command=self.square)
            elif text == "1/x":
                button.config(command=self.inverse)
            else:
                button.config(command=lambda t=text: self.display.insert(tk.END, t))

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

    def on_button_click(self, text):
        if text in ["sin", "cos", "tan", "asin", "acos", "atan", "sinh", "cosh", "asinh", "acosh"]:
            self.display.insert(tk.END, f"{text}(")
        elif text == "log":
            self.display.insert(tk.END, "log10(")
        elif text == "^":
            self.display.insert(tk.END, "**")
        elif text == "√":
            self.display.insert(tk.END, "sqrt(")
        elif text == "exp":
            self.display.insert(tk.END, "exp(")
        elif text == "π":
            self.display.insert(tk.END, "pi")
        elif text == "e":
            self.display.insert(tk.END, "e")
        elif text == "^2":
            self.display.insert(tk.END, "**2")
        elif text == "1/x":
            self.display.insert(tk.END, "1/")
        else:
            self.display.insert(tk.END, text)

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

    def clear_all(self):
        self.display.delete(0, tk.END)

    def trigonometric_function(self, func):
        value = self.display.get()
        try:
            result = getattr(math, func)(math.radians(float(value)))
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

    def power(self):
        base = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, base+"**")

    def square_root(self):
        value = self.display.get()
        try:
            result = math.sqrt(float(value))
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

    def pi(self):
        self.display.insert(tk.END, "pi")

    def e(self):
        self.display.insert(tk.END, "e")

    def square(self):
        value = self.display.get()
        try:
            result = float(value) ** 2
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

    def inverse(self):
        value = self.display.get()
        try:
            result = 1 / float(value)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

# Cria a janela principal
root = tk.Tk()
app = Calculator(root)
root.mainloop()
