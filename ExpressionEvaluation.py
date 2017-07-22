class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class ExpressionEvaluation:
    def __init__(self):
        self.ops = Stack()
        self.values = Stack()

    def evaluate_string(self, strs):
        i = 0
        while i < len(strs):
            #print strs[i]

            # Current char is whitespace, skip it
            if strs[i].isspace():
                continue

            # Current token is a number, push it to stack for numbers
            if ord(strs[i]) >= ord('0') and ord(strs[i]) <= ord('9'):
                digit = ""
                while i < len(strs) and strs[i] >= '0' and strs[i] <= '9':
                    digit = digit + strs[i]
                    i += 1
                self.values.push(int(digit))
                continue

            # Current token is an opening brace, push it to 'ops'
            if strs[i] == '(':
                self.ops.push(strs[i])
            # Closing brace encountered, solve entire brace
            if strs[i] == ')':
                while self.ops.peek() != '(':
                    operator = self.ops.pop()
                    b = self.values.pop()
                    a = self.values.pop()
                    self.values.push(self.applyOp(operator, b, a))
                self.ops.pop()

            # Current token is an operator
            if strs[i] in "+-*/":
                # While top of 'ops' has same or greater precedence to current token, which is an operator.
                # Apply operator on top of 'ops' to top two elements in values stack
                while not self.ops.isEmpty() and self.hasPrecedence(strs[i], self.ops.peek()):
                    res = self.applyOp(self.ops.pop(), self.values.pop(), self.values.pop())
                    #print res
                    self.values.push(res)
                self.ops.push(strs[i])
            i += 1

        # Entire expression has been parsed at this point, apply remaining ops to remaining values
        while not self.ops.isEmpty():
            self.values.push(self.applyOp(self.ops.pop(),self.values.pop(),self.values.pop()))

        # Top of 'values' contains result, return it
        return self.values.pop()

    # Returns true if 'op2' has higher or same precedence as 'op1',
    # otherwise returns false.
    def hasPrecedence(self, op1, op2):
        if op2 in "()":
            return False
        if op1 in "*/" and op2 in "+-":
            return False
        else:
            return True

    # A utility method to apply an operator 'op' on operands 'a' and 'b'. Return the result.
    def applyOp(self, op, b, a):
        if op == '+':
            return a+b
        elif op == '-':
            return a-b
        elif op == '*':
            return a*b
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError("Please check the expression")
            return a/b
        else:
            return 0


if __name__ == '__main__':
    ob = ExpressionEvaluation()
    print ob.evaluate_string("10*(2+12)/14")
    print ob.evaluate_string("2*8-(100/50)+6")


