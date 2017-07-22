class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]


def balancedBrackets(sym_str):
    s = Stack()
    index = 0
    balanced = True
    if sym_str in "":
        return True
    else:
        while index in range(len(sym_str)) and balanced:
            char = sym_str[index]
            if not char.isalnum():
                if char in "[{(":
                    s.push(char)
                else:
                    if s.isEmpty():
                        balanced = False
                    else:
                        top = s.pop()
                        if not matches(top, char):
                            balanced = False
            index += 1
    if s.isEmpty() and balanced:
        return True
    else:
        return False


def matches(open, close):
    # print open
    open_braces = '[{('
    close_braces = ']})'
    return open_braces.index(open) == close_braces.index(close)


def test():
    print balancedBrackets("{{([][])}()}")
    print balancedBrackets('[{()]')
    print balancedBrackets('{{hsaghas(sdfsdbjf}}dhfsgdj)')


if __name__ == '__main__':
    test()
