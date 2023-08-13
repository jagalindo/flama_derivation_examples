from flask import Flask, render_template, request
import math
import json

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

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ''
    if request.method == 'POST':
        operation = OPERATIONS.get(request.form.get('operation'))
        if operation:
            try:
                num1 = float(request.form.get('num1'))
                if operation['needs_two_nums']:
                    num2 = float(request.form.get('num2'))
                    result = operation['func'](num1, num2)
                else:
                    result = operation['func'](num1)
            except ValueError:
                result = "Invalid input or calculation."
    return render_template('index.html', operations=OPERATIONS, flags=FEATURE_FLAGS, result=result)

if __name__ == '__main__':
    app.run(debug=True)
