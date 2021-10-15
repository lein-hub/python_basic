count = int(input())

result = []

for _ in range(count):
    num = int(input())
    if num != 0:
        result.append(num)
    else:
        result.pop()

print(sum(result))
