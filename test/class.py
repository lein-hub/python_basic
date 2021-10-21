# class Student:
#     name = '동재'

#     def __init__(self, name):
#         self.name = name
#         print("I'm", name)

#     def say_hello(self):
#         print('Hello')

#     @classmethod
#     def create_student(cls, name):
#         return cls(name)


# s1 = Student('ABC')
# s1.say_hello()

# Student.say_hello(s1)
# s2 = Student.create_student('BCD')


class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def __del__(self):
        print('delete circle')

    def __repr__(self):
        return 'circle'

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def __dq__(self, other):
        if self.r == other.r and self.x == other.x and self.y == other.y:
            return True
        else:
            return False


# c1 = Circle()
# c2 = Circle(0, 0, 2)
# print(c1, c2)

# print(dir())
# print(dir(c2))

class MyClass:
    message = 'hello'

    def __init__(self, name):
        self.name = name


# print(id(MyClass.message))
a = MyClass('a')
# print(a.name, id(a.name), a.message, id(a.message))
b = MyClass('b')
# print(b.name, id(b.name), b.message, id(b.message))
# MyClass.message = 'bye'
# print(a.message, b.message)

a.message = 'bye'
print(id(MyClass.message), id(a.message), id(b.message))


class Member:
    def __init__(self, id='0'):
        self.member_id = id

    def __repr__(self):
        return 'member_id = ' + self.member_id


# class Student(Member):
#     pass

class Student(Member):
    def __init__(self, major='computer'):
        super().__init__()
        self.major = major

    def __repr__(self):
        return 'major = ' + self.major + ' ' + self.member_id


s = Student('zero')
print(s)
