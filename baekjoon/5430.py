import sys

tries = int(sys.stdin.readline().rstrip())

result = ''

for x in range(tries):
    funcs = list(sys.stdin.readline().rstrip())
    num_count = int(sys.stdin.readline().rstrip())
    num_list = sys.stdin.readline().rstrip(
    )[1:-1].split(',')
    if num_count == 0:
        num_list = []

    is_error = False
    is_reversed = False

    for i in funcs:
        if i == 'R':
            is_reversed = not is_reversed
        elif i == 'D':
            if len(num_list) == 0:
                is_error = True
                break
            else:
                if is_reversed:
                    num_list.pop()
                else:
                    num_list.pop(0)
    if is_error:
        result += 'error' + '\n'
    elif not is_reversed:
        result += '[' + ','.join(num_list) + ']' + '\n'
    else:
        result += '[' + ','.join(num_list[::-1]) + ']' + '\n'

print(result)
