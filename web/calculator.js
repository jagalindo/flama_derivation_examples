const OPERATIONS = {
    add: {func: (a, b) => a + b, label: '+', needsTwoNums: true},
    subtract: {func: (a, b) => a - b, label: '-', needsTwoNums: true},
    multiply: {func: (a, b) => a * b, label: '*', needsTwoNums: true},
    divide: {func: (a, b) => a / b, label: '/', needsTwoNums: true},
    sqrt: {func: (a) => Math.sqrt(a), label: 'sqrt', needsTwoNums: false},
    exp: {func: (a, b) => Math.pow(a, b), label: '^', needsTwoNums: true},
    modulus: {func: (a, b) => a % b, label: '%', needsTwoNums: true},
    absolute: {func: (a) => Math.abs(a), label: '|a|', needsTwoNums: false},
    log: {func: (a, b) => Math.log(a) / Math.log(b), label: 'log', needsTwoNums: true},
    factorial: {func: (a) => factorial(a), label: '!', needsTwoNums: false},
};

function factorial(n) {
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

let selectedOperation = null;

for (let [opName, operation] of Object.entries(OPERATIONS)) {
    if (FEATURE_FLAGS[opName]) {
        let button = document.createElement('button');
        button.textContent = operation.label;
        button.onclick = () => { selectedOperation = operation; };
        document.getElementById('operations').appendChild(button);
    }
}

function calculate() {
    if (selectedOperation) {
        let num1 = parseFloat(document.getElementById('num1').value);
        let num2 = selectedOperation.needsTwoNums ? parseFloat(document.getElementById('num2').value) : undefined;
        let result = selectedOperation.func(num1, num2);
        document.getElementById('output').textContent = isNaN(result) ? 'Error' : result;
    }
}
