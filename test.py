from functools import reduce
import os


# name = input()
name = 1
print(name)

print(100 + 200)

name = "尹超"
print(name.encode().decode())
print(len(name))
print(len(name.encode()))  # 计算字节数

name = "abcd"
print(name.encode(encoding="ascii").decode())
print(len(name))

# 字符串格式化输出
print("age: %s, gender: %s" % (25, "male"))

# 容器, list
list_yc = list()
list_yc.append("yinchao")
list_yc.append("wsyinchao")
list_yc.append(1)
list_yc.insert(1, 2)
# list_yc.sort()
print(list_yc)
# 容器, list..列表生成器
list_yc = list(x * x for x in range(1, 10) if x % 2 == 0)
print(list_yc)
# 两层for循环
list_yc = list(
    m + n + q + p for m in "yc" for n in "dqwj" for q in "jzmb" for p in "sww")
print(list_yc)
# 应用
list_yc = os.listdir()
print(list_yc)
# 生成器_斐波那契数列


def flib(item_count):
    if item_count == 1:
        return 0
    elif item_count == 2:
        return 1

    item_count = item_count - 2
    a, b = 0, 1
    n = 0
    while n < item_count:
        yield b  # 加上关键字 yield, flib就变成了generator
        a, b = b, a + b
        n = n + 1
    return b


for v in flib(10):
    print(v)

# 生成器_杨辉三角


def triangles():
    res = [1]
    while True:
        yield res
        res.append(0)
        res = [res[i] + res[i - 1] for i in range(len(res))]


n = 0
for v in triangles():
    print(v)
    n = n + 1
    if n == 10:
        break

list_yc = list(range(2))  # [0, 1]
print(list_yc)

# tuple
tuple_yc = (1, 2, 3, 4)
# tuple_yc.append(1)  # tuple不允许改变
print(tuple_yc)

# loop
sum_yc = 0
for x in range(100):
    sum_yc = sum_yc + x

print(sum_yc)
print(sum(range(1, 1000)))

# loop2
n = 100
sum_yc = 0
while n > 10:
    sum_yc = sum_yc + n
    n = n - 10

print(sum_yc)

# dict and set
dict_yc = dict()
dict_yc["yinchao"] = "尹超"
dict_yc["daqiaoweijiu"] = "大桥未久"
dict_yc["dqwj"] = "大桥未久"

print(dict_yc["daqiaoweijiu"])
if "chuancunzhenshi" in dict_yc:
    print(True)
else:
    print(False)

name = dict_yc.get("dqwj", -1)
if name != -1:
    print("dqwj is exist!")

set_yc = set()
set_yc.add(1)
set_yc.add(2)
set_yc.add(2)

print(set_yc)

list_yc = list(set_yc)
list_yc.sort(reverse=True)
print(list_yc)

# func


def abc_yc(x):
    if x >= 0:
        return x
    else:
        return -x


print(abc_yc(-1))

# 切片
list_yc = list(range(100))
print(list_yc[::5])
print(list_yc[::2])
print(list_yc[0:15])
print(list_yc[0:3])  # 取前三个数

# 迭代
dict_yc = dict()
dict_yc["dqwj"] = "大桥未久"
dict_yc['yc'] = "尹超"
dict_yc['linux'] = "Linus Torvalds"

for key in dict_yc:
    print(key)
    print(dict_yc[key])


# map & reduce
def f(x):
    return x * x


list_yc = list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(list_yc)


def f2(a, b):
    return a * 10 + b


variable_yc = reduce(f2, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(variable_yc)

# 应用


def char2Num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, }
    return digits[s]


variable_yc = reduce(f2, map(char2Num, '4573950342'))  # 字符串转化为数字
print(variable_yc)

# 练习


def normalLize(name):
    # lower
    # upper
    # title
    return name.capitalize()


list_yc = list(map(normalLize, ['LSKDJ', 'sldgj', 'lkjLKJihJhOlk']))
print(list_yc)

# filter


def is_odd(x):
    if x % 2 == 0:
        return True
    return False


list_yc = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(list_yc)

variable_yc = 'sd'

# return the copy of string s with leading and trailing whitespave removed.
# variable_yc.strip()

# 应用，求素数 #######################


def _odd_iter():  # 构建奇数序列 从3开始
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0
    # def lam(x):
    #     return x % n > 0
    # return lam
    # need iterator, and tracking & debugging


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)  # 返回序列中的数
        yield n
        it = filter(_not_divisible(n), it)


list_yc = list()
for n in primes():
    if n > 15:
        break
    list_yc.append(n)

print(list_yc)
name = input()
