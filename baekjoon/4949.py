import sys

result = ''

while True:
    text = sys.stdin.readline().rstrip()
    if text == '.':
        break

    balanced = True
    brackets = []

    for i in text:
        if i in ['[', '(']:
            brackets.append(i)
        elif i == ']':
            if len(brackets) == 0 or brackets[-1] != '[':
                balanced = False
                break
            else:
                brackets.pop()
        elif i == ')':
            if len(brackets) == 0 or brackets[-1] != '(':
                balanced = False
                break
            else:
                brackets.pop()

    if balanced and len(brackets) == 0:
        result += 'yes\n'
    else:
        result += 'no\n'

print(result)
