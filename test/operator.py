# a, b, c, d = 20, 30, 6, 2
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/d)
# print(a % c)
# print(c**d)
# print(a//c)

# a, b, c = True, False, True

# print(a and b)
# print(a and c)
# print(a or b)
# print(not a)

# num = int(input())
# if num < 0:
#     print('NG')
# else:
#     print('OK')

# str = input()
# if len(str) >= 8:
#     print('OK')
# else:
#     print('NG')

# list = input().split()
# num1, num2 = int(list[0]), int(list[1])
# if num1 > 0 and num2 > 0 or num1 < 0 and num2 < 0:
#     print('OK')
# else:
#     print('NG')

# num = int(input())
# if num % 2 == 0:
#     print('even')
# else:
#     print('odd')

# str = input()
# if 10 >= len(str) >= 4:
#     print('OK')
# else:
#     print('NG')

# num1, num2 = map(int, input().split())
# print('OK') if num1 + num2 >= 0 else print('NG')

# num1, num2 = map(int, input().split())
# opr = input()
# print(num1 + num2) if opr == '+' else print(num1 - num2)

# arr = [1, 3, 5, 7]
# for a in arr:
#     print(a)
# for b in [2, 4, 6, 8]:
#     print(b)
# for c in arr[2:]:
#     print(c)

# tp = (1, 2, 3, 4, 5)
# for t in tp:
#     print(t)
# str = 'Hello everyone'
# for s in str:
#     print(s)

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for a in arr:
#     if a % 2 == 0:
#         print(a)

# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# odd_sum, even_sum = 0, 0
# for a in arr:
#     if a % 2 == 0:
#         even_sum += a
#     else:
#         odd_sum += a
# print(odd_sum)
# print(even_sum)

# for a in range(2, 10):
#     print(2, 'x', a, '=', 2 * a)

# for i in range(0, 4):
#     for j in range(0, 4):
#         if i-j >= 0:
#             print('*', end='')
#     print()

# arr = ['John', 'Kate', 'Sam']
# for i, v in enumerate(arr):
#     print(i, v)

# arr1 = [10, 11, 12, 13]
# arr2 = [1, 2, 3, 4]
# arr3 = ['hello', 'my', 'friend']
# for i, j, k in zip(arr1, arr2, arr3):
#     print(i, j, k)

# arr = [i for i in range(5, 10)]
# print(arr)
# arr = [i*2 for i in range(3)]
# print(arr)
# arr = [[i, j] for i in range(3) for j in range(10, 13)]
# print(arr)

# arr = [i for i in range(1, 11, 2)]
# print(arr)
# arr = [i*3 for i in range(1, 11)]
# print(arr)

# arr = [i for i in range(10) if i % 2 == 0]
# print(arr)
# scores = [80, 95, 66, 88, 90, 70, 74, 98]
# a_grade = [s for s in scores if s >= 90]
# print(a_grade)

# size = int(input())
# arr = []
# for i in range(size):
#     arr.append(int(input()))
# arr2 = [a for a in arr if a >= 0]
# for a in arr2:
#     print(a)

# set1 = {i for i in range(5)}
# print(set1)
# arr = [1, 1, 1, 2, 2, 3, 3, 3]
# set2 = {i for i in arr}
# print(set2)

# arr_id = ['12101', '12102', '12103', '12104']
# arr_score = [80, 90, 90, 70, 80]
# dic = {key: value for key, value in zip(arr_id, arr_score)}
# print(dic)
# dic = {key: value for key, value in zip(arr_id, arr_score) if value > 80}
# print(dic)

# val = 10
# while val > 0:
#     print(val)
#     val -= 1

# while True:
#     print('Enter Number', end=" ")
#     value = int(input())
#     if value < 0:
#         break

# sum = 0
# for i in range(5):
#     val = int(input())
#     if val < 1:
#         pass
#     else:
#         sum += val
#     print(i, sum)
# print('final value', sum)

sum = 0
while True:
    val = int(input())
    if val == 0:
        break
    sum += val
print(sum)
