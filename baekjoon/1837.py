key, judge = map(int, input().split())
result = 'GOOD'

numbers = [True] * judge
numbers[0], numbers[1] = False, False

for i in range(2, judge):
    if numbers[i]:
        for j in range(i*2, judge, i):
            if numbers[j]:
                numbers[j] = False

for x in range(2, judge):
    if not numbers[x]:
        continue
    if key % x == 0:
        result = 'BAD ' + str(x)
        break

print(result)
