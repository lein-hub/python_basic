key, judge = map(int, input().split())
result = 'GOOD'

for x in range(2, judge):
    if key % x == 0:
        result = 'BAD ' + str(x)
        break

print(result)
