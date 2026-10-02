import ast
import operator
import tkinter as tk
from tkinter import ttk


def calculate(expression):
    if len(expression) > 1000:
        raise ValueError('Слишком длинное выражение.')
    operations = {ast.Add: operator.add, ast.Sub: operator.sub,
                  ast.Mult: operator.mul, ast.FloorDiv: operator.floordiv,
                  ast.Mod: operator.mod}

    def evaluate(node):
        if isinstance(node, ast.Constant) and type(node.value) is int:
            return node.value
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
            value = evaluate(node.operand)
            return -value if isinstance(node.op, ast.USub) else value
        if isinstance(node, ast.BinOp) and type(node.op) in operations:
            return operations[type(node.op)](evaluate(node.left), evaluate(node.right))
        raise ValueError('Допустимы целые числа, скобки и операции +, -, *, //, %.')

    return evaluate(ast.parse(expression.strip(), mode='eval').body)


def create_app():
    root = tk.Tk()
    root.title('Калькулятор')
    frame = ttk.Frame(root, padding=20)
    frame.pack(fill='both', expand=True)
    expression = tk.StringVar()
    result = tk.StringVar(value='Введите выражение')
    ttk.Label(frame, text='Выражение').pack(anchor='w')
    entry = ttk.Entry(frame, textvariable=expression, width=45)
    entry.pack(fill='x', pady=8)

    def submit(event=None):
        try:
            result.set(str(calculate(expression.get())))
        except ZeroDivisionError:
            result.set('Деление на ноль невозможно.')
        except (ValueError, SyntaxError, RecursionError, OverflowError):
            result.set('Проверьте выражение: целые числа, +, -, *, //, %, скобки.')

    ttk.Button(frame, text='Вычислить', command=submit).pack(pady=8)
    ttk.Label(frame, textvariable=result, wraplength=420).pack(pady=8)
    root.bind('<Return>', submit)
    entry.focus_set()
    return root


if __name__ == '__main__':
    create_app().mainloop()
