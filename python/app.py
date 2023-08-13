import json
import tkinter as tk
from tkinter import messagebox
import math

# Load feature flags from .features file
with open('.features') as f:
    FEATURE_FLAGS = json.load(f)

# Define operations
OPERATIONS = {
    'add': {'func': lambda a, b: a + b, 'label': '+', 'needs_two_nums': True},
    'subtract': {'func': lambda a, b: a - b, 'label': '-', 'needs_two_nums': True},
    'multiply': {'func': lambda a, b: a * b, 'label': '*', 'needs_two_nums': True},
    'divide': {'func': lambda a, b: a / b if b != 0 else None, 'label': '/', 'needs_two_nums': True},
    'sqrt': {'func': lambda a: math.sqrt(a) if a >= 0 else None, 'label': 'sqrt', 'needs_two_nums': False},
    'exp': {'func': lambda a, b: a ** b, 'label': '^', 'needs_two_nums': True},
    'modulus': {'func': lambda a, b: a % b if b != 0 else None, 'label': '%', 'needs_two_nums': True},
    'absolute': {'func': lambda a: abs(a), 'label': '|a|', 'needs_two_nums': False},
    'log': {'func': lambda a, b: math.log(a, b) if a > 0 and b > 0 else None, 'label': 'log', 'needs_two_nums': True},
    'factorial': {'func': lambda a: math.factorial(int(a)) if a >= 0 else None, 'label': '!', 'needs_two_nums': False},
}

def calculate(operation):
    try:
        num1 = float(entry1.get())
        if operation['needs_two_nums']:
            num2 = float(entry2.get())
            result = operation['func'](num1, num2)
        else:
            result = operation['func'](num1)

        if result is None:
            raise ValueError("Invalid calculation.")
        else:
            result_label.config(text="Result: " + str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input or calculation.")

root = tk.Tk()

entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

result_label = tk.Label(root)
result_label.pack()

# Create buttons based on feature flags
for op_name, operation in OPERATIONS.items():
    if FEATURE_FLAGS.get(op_name, False):
        button = tk.Button(root, text=operation['label'], command=lambda op=operation: calculate(op))
        button.pack()

root.mainloop()
