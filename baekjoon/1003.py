cases = int(input())
arr = [int(input()) for _ in range(cases)]

max_num = max(arr)
result = [[0, 0] for _ in range(max_num+1)]
result[0] = [1, 0]
result[1] = [0, 1]

if max_num > 1:
    for n in range(2, max_num + 1):
        num0 = result[n-1][0] + result[n-2][0]
        num1 = result[n-1][1] + result[n-2][1]

        result[n] = [num0, num1]

for a in arr:
    print(result[a][0], result[a][1])
