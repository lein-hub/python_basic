# def say_hello():
#     print('hello')
# def say_bye(name):
#     print('bye,', name)
# say_hello()
# say_bye('Tim')

##########################################################

# def add(first, second):
#     print(first, '+', second, '=', first+second)
# add(1, 2)
# add(10, 20)
# add(second=1, first=2)

##########################################################

# num1 = int(input())
# num2 = int(input())
# def bigger(num1, num2):
#     if num1 > num2:
#         return print(num1)
#     return print(num2)
# bigger(num1, num2)

##########################################################

# def hello(age, name='user'):
#     print('hello', name, age)
# hello(20)
# hello(20, 'abc')

##########################################################

# def print_tp(*t):
#     print(t)
# def print_dic(**d):
#     print(d)
# print_tp(1, 2, 3, 4, 5)
# print_dic(first=1, second=2, third=3)

##########################################################

# def sum_int(*t):
#     sum = 0
#     for x in t:
#         if type(x) is int:
#             sum += x
#     print(sum)
# sum_int(1, 1, 1.0, '1', 'True')

##########################################################

# # 가변변수와 일반변수를 함께 사용할 경우 가변변수 뒤쪽에 있는 일반변수는 이름을 지정해 줘야한다.

# def param1(a, b, c=5, *t):
#     print(c)
#     print(t)


# def param2(a, *t, b, c=3):
#     print(c)
#     print(t)


# def param3(*t, a, b, c=3):
#     print(c)
#     print(t)


# param1(1, 2, 3, 4)  # 3이 c로 전달된다
# param2(1, 2, 3, b=4)  # 2, 3이 튜플로 전달된다
# param3(1, 2, a=3, b=5, c=6)  # 이름을 지정하기 전까지 튜플로 전달된다

##########################################################

# def func(second, first):
#     print(second, first)


# param1 = [1, 2]
# param2 = (3, 4)
# func(*param1)
# func(*param2)
# func(*[5, 6])


# def func(first, second):
#     print(first, second)


# dic = {'first': 1, 'second': 2}
# func(**dic)

##########################################################

# 다양한 타입 반환가능

# def int_func():
#     return 1


# def float_func():
#     return 1.1


# def list_func():
#     return [1, 2, 3]


# def set_func():
#     return {1, 2, 3}


# def tuple_func():
#     return 1, 2, 3


# def dic_func():
#     return {1: 1, 2: 2, 3: 3}


# print(int_func(), type(int_func()))

##########################################################

# list = [1, 2, 3, 4, 5]


# def mini(list):
#     return min(list)


# def mini(list):
#     min = list[0]
#     for i in list[1:]:
#         if i < min:
#             min = i
#     return min


# print(mini(list))

##########################################################

# def func():
#     return 1, 2, 3


# tp = func()
# print(type(tp))
# x, y, z = func()
# x = 10
# print(x, y, z)

##########################################################

# def info(list):
#     return sum(list), sum(list) / len(list)


# list = [1, 3, 4, 5]
# sum, avg = info(list)
# print(sum, avg)

##########################################################

# def min_max(list):
#     return min(list), max(list)


# list = [1, 3, 4, 5]
# min, max = min_max(list)
# print(min, max)

##########################################################

# sum = 0


# def total(values):
#     global sum
#     for i in values:
#         sum += i
#     print(sum)


# total([1, 2, 3])
# print(sum)

##########################################################

# # mutable: list, dictionary, set -> 원본이 수정됨
# # immutable: number, string, tuple -> 원본이 수정되지 않음

# def func(first, second):
#     first += 10
#     second.add(4)


# number = 1
# set = {1, 2, 3}
# func(number, set)
# print(number, set)

##########################################################

# def count_down(n):
#     if n == 0:
#         return
#     print(n)
#     count_down(n-1)


# count_down(5)

##########################################################

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result


# def rc_factorial(n, d=1):
#     if n == 1:
#         return d
#     d *= n
#     return rc_factorial(n-1, d)


# print(factorial(1))
# print(factorial(3))
# print(factorial(5))
# print(rc_factorial(1))
# print(rc_factorial(3))
# print(rc_factorial(5))

##########################################################

# def print_items(param):
#     for p in param:
#         print(p)


# print_items((i for i in range(3)))

##########################################################

# def my_generator():
#     print('1반환')
#     yield 1
#     print('2반환')
#     yield 2
#     print('3반환')
#     yield 3


# list = [i for i in my_generator()]
# print(list)

# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))


##########################################################

# def my_range(*num):
#     step = 1
#     if len(num) == 1:
#         start = 0
#         end = num[0]
#     elif len(num) >= 2:
#         start = num[0]
#         end = num[1]
#         if len(num) > 2:
#             step = num[2]

#     while start < end:
#         yield start
#         start += step


# list1 = [i for i in my_range(5)]
# list2 = [i for i in my_range(2, 5)]
# list3 = [i for i in my_range(1, 10, 2)]
# print(list1)
# print(list2)
# print(list3)

##########################################################

# def add(first, second):
#     return first+second


# def sub(first, second):
#     return first-second


# def executor(func, param1, param2):
#     return func(param1, param2)


# func = {'+': add, '-': sub}
# print(executor(func['+'], 1, 2))
# print(executor(func['-'], 1, 2))

##########################################################

# def add(first, second):
#     return first+second


# def sub(first, second):
#     return first-second


# def get_func(op):
#     if op == '+':
#         return add
#     else:
#         return sub


# result = get_func('+')(1, 2)
# print(result)

##########################################################

# def calculate(op, num1, num2):
#     def add(num1, num2):
#         return num1 + num2

#     def sub(num1, num2):
#         return num1 - num2

#     if op == '+':
#         return add(num1, num2)
#     else:
#         return sub(num1, num2)


# print(calculate('-', 1, 2))

##########################################################

# def calculate(op):
#     def add(num1, num2):
#         return num1 + num2

#     def sub(num1, num2):
#         return num1 - num2

#     if op == '+':
#         return add
#     else:
#         return sub


# print(calculate('-')(1, 2))

##########################################################

# def func():
#     value = 2

#     def nested_func():
#         value = 3
#         print('nested', value)
#     nested_func()
#     print('outer', value)


# func()

##########################################################

# def func():
#     value = 2

#     def nested_func():
#         nonlocal value
#         value = 3
#         print('nested', value)
#     nested_func()
#     print('outer', value)


# func()


# def func():
#     value = 2

#     def nested_func():
#         print('nested', value)
#     nested_func()
#     print('outer', value)


# func()

##########################################################

# def func():
#     print('hello')


# def func():
#     print('bye')


# func()

# if int(input()) == 1:
#     def func():
#         print('hello')
# else:
#     def func():
#         print('bye')

# func()

##########################################################

# def scale_up():
#     scale = 10

#     def calculate(number):
#         return number*scale
#     return calculate


# func = scale_up()
# print(func(5))

##########################################################

# num = 0
# try:
#     num = int(input())
# except ValueError:
#     num = 0
# finally:
#     print(num)

##########################################################

# list = [1, 2, 3]
# value = 0
# try:
#     index = int(input())
#     value = list[index]
# except (ValueError, IndexError):
#     value = list[0]
# print(value)

##########################################################

# dict = {1: 'one', 2: 'two'}
# num1 = int(input())
# num2 = int(input())
# try:
#     value = 10/num1
#     value2 = dict[num2]
# except ZeroDivisionError as error1:
#     print(error1)
# except KeyError as error2:
#     print(error2)
# else:
#     print(value, value2)

##########################################################

# def add(first, second):
#     if type(first) is not int or type(second) is not int:
#         raise TypeError
#     return first + second


# try:
#     add('1', 1)
# except TypeError:
#     print('not supported data type')

##########################################################

# def b_search(value, list):
#     low, high = 0, len(list) - 1
#     while low <= high:
#         mid = (low+high) // 2
#         if list[mid] == value:
#             return mid
#         if list[mid] > value:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return -1


# lst = [1, 3, 6, 9, 12, 15, 18, 21]
# print('result index = ', b_search(6, lst))

##########################################################

# lst = [None for _ in range(10)]
# size = len(lst)
# top = -1

# def push(value):
#     global top
#     if top < size - 1:
#         top += 1
#         lst[top] = value
#     else:
#         print('stack overflow')

# def pop():
#     global top
#     if top > -1:
#         value = lst[top]
#         del lst[top]
#         top -= 1
#         return value
#     else:
#         print('stack empty')


def my_range(*t):
    length = len(t)
    start = 0
    step = 1
    if length == 1:
        end = t[0]
    elif length == 2:
        start = t[0]
        end = t[1]
    elif length == 3:
        start = t[0]
        end = t[1]
        step = t[2]

    while start < end:
        yield start
        start += step
