class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        operations = {"/", "+", "-", "*"}
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                second_op = stack.pop()
                first_op = stack.pop()
                if token == "/":
                    res = int(first_op/second_op)
                if token == "*":
                    res = first_op * second_op
                if token == "+":
                    res = first_op + second_op
                if token == "-":
                    res = first_op - second_op
                stack.append(res)
        return stack.pop()