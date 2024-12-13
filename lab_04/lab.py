def rpn(expression):
    result = []
    stack = []

    precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    current_number = ""

    for char in expression:
        if char.isspace():
            continue

        if char.isdigit():
            current_number += char
        else:
            if current_number:
                result.append(int(current_number))
                current_number = ""

            if char in precedence:
                while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[char]:
                    result.append(stack.pop())
                stack.append(char)

            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()

    if current_number:
        result.append(int(current_number))

    while stack:
        result.append(stack.pop())

    return result

def evaluate_rpn(rpn_list):
    stacks = []

    for token in rpn_list:
        if isinstance(token, int):
            stacks.append(token)
        else:
            if len(stacks) < 2:
                raise ValueError("Invalid expression: insufficient operands for the operator.")
            right = stacks.pop()
            left = stacks.pop()

            if token == '+':
                stacks.append(left + right)
            elif token == '-':
                stacks.append(left - right)
            elif token == '*':
                stacks.append(left * right)
            elif token == '/':
                if right == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                stacks.append(left / right)
            elif token == '^':
                stacks.append(left ** right)

    if len(stacks) != 1:
        raise ValueError("Invalid expression: extra operands remain.")

    return stacks[0]

def main():
    try:
        user_expression = input("Enter a mathematical expression: ")
        rpn_result = rpn(user_expression)
        print(f"Reverse Polish Notation: {' '.join(map(str, rpn_result))}")
        print(f"Result: {evaluate_rpn(rpn_result)}")
    except Exception as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
