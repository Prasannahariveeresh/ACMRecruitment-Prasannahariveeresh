class Calculator:

    def __init__(self):
        self.get_history = []

        self.__precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, 'sqrt': 4}

    def evaluate(self, expr):
        tokens = self._tokenizer(expr)

        if '(' in expr:
            tokens = self._eval_parentheses(tokens)

        while len(tokens) > 1:
            op_idx, operator =  self._next_operation(tokens)
            res = self._apply_operation(operator, op_idx, tokens)

            if op_idx == 0:
                tokens = [] + [str(res)] + tokens[op_idx+2:]
            else:
                tokens = tokens[:op_idx-1] + [str(res)] + tokens[op_idx+2:]

        return float(tokens[0])

    def _eval_parentheses(self, tokens):
        open = -1
        close = -1

        for i, token in enumerate(tokens):
            if token == '(':
                open = i
            if token == ')':
                close = i
                break

        if open != -1 and close != -1:
            inside_parentheses = ''.join(tokens[open+1 : close])
            parentheses_res = self.evaluate(inside_parentheses)

            tokens = tokens[:open] + [str(parentheses_res)] + tokens[close + 1:]

        return tokens

    def _next_operation(self, tokens):
        max_prece = -1
        op_idx = -1
        op = ''

        for i, token in enumerate(tokens):
            if token in self.__precedence and self.__precedence[token] > max_prece:
                max_prece = self.__precedence[token]
                op_idx = i
                op = token

        return op_idx, op

    def _apply_operation(self, op, i, tokens):
        if op == 'sqrt':
            return float(tokens[i + 1])**(0.5)

        left_op = float(tokens[i - 1])
        right_op = float(tokens[i + 1])

        if op == '+':
            return left_op + right_op
        elif op == '-':
            return left_op - right_op
        elif op == '*':
            return left_op*right_op
        elif op == '/':
            if right_op == '0':
                raise ZeroDivisionError('Division by Zero is not allowed')

            return left_op/right_op
        elif op == '^':
            return left_op**right_op
        else:
            raise ValueError(f'Unknown operator {op} is parsed')

    def _tokenizer(self, expression):
        tokens = []
        num = ''
        i = 0
        while i < len(expression):
            if expression[i].isdigit() or expression[i] == '.':
                num += expression[i]
            else:
                if num:
                    tokens.append(num)
                    num = ''
                if expression[i:i+4] == 'sqrt':
                    tokens.append('sqrt')
                    i += 3
                elif expression[i] in '+-*/^()':
                    tokens.append(expression[i])
                elif expression[i] == ' ':
                    pass
                else:
                    raise ValueError(f"Unexpected character: {expression[i]}")
            i += 1
        if num:
            tokens.append(num)  # Append the last collected number
        return tokens

if __name__ == '__main__':

    print("""
    Welcome to Calculator App !! Press
        1. To Calculate
        2. View History
        3. Exit
    """)

    calc_obj = Calculator()

    while True:
        val = input("Enter the task to complete: ")
        if val == '1':
            expr = input("\nEnter your expression: ")
            res = calc_obj.evaluate(expr)
            calc_obj.get_history.append((expr, res))

            print("Answer to the expression is: ", res)

        elif val == '2':
            for i, obj in enumerate(calc_obj.get_history):
                print(f'Question {i+1}\n\t{obj[0]} = {obj[1]}')

        elif val == '3':
            break