
# import statistics as st
import random as rd
import math
import os


# value = rd.random()
# value2 = rr()
# print(value)
# print(value2)

# print(os.name)
# print(os.getcwd())
# os.system('notepad')


print('log', math.log(8, 2))
print('pi', math.pi)

print('sample', rd.sample(range(100), 10))
print('rand float', rd.random())
print('rand int', rd.randint(10, 100))
data = [i for i in range(1, 11)]
data.append(100)
print(data)
print('choice', rd.choice(data))

# print('mean', st.mean(data))
# print('median', st.median(data))
# print('variance', st.variance(data))
# print('stdev', st.stdev(data))
