# ce1_interpreter.py
"""
Simple CE1 interpreter example.
This interpreter supports basic arithmetic.
"""

def interpret(expression):
    tokens = expression.split()
    # Only handle simple expressions: number1 operator number2
    if len(tokens) != 3:
        raise ValueError("Invalid expression")
    num1, op, num2 = tokens
    num1 = float(num1)
    num2 = float(num2)
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2
    else:
        raise ValueError(f"Unknown operator {op}")

if __name__ == "__main__":
    expr = input("Enter expression (e.g., '2 + 3'): ")
    result = interpret(expr)
    print(f"Result: {result}")
