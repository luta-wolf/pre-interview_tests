# Реши задачу
# Дается строка в которой дается любое количество любых скобок (, [, {, }, ], )
# Строка считается правильной, если для каждой открывающей скобочки есть закрывающая на положенном месте и не правильной, если такой скобочки нет.
string = '([{}]())'
string2 = '()((}}'
string3 = ')([{}]())('
string4 = '())()(()())(()'


def check_brackets(s):
    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        elif c in ')]}':
            if not stack:
                return "Bruh"
            if c == ')' and stack[-1] == '(' or \
               c == ']' and stack[-1] == '[' or \
               c == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return "Bruh"
    return "Nice" if not stack else "Bruh"

print(check_brackets(string))
print(check_brackets(string2))
print(check_brackets(string3))
print(check_brackets(string4))
