# №1
a = [1, 2, 3]
b = [5, 6]

# ab = [(a_v, b[a_i]) for a_i, a_v in enumerate(a)]
# ab = [(a_v, b_v) for a_v in a for b_v in b]
ab = zip(a, b)
print(list(ab))

# ----------------------------------------------------
# №2
def my_dec(a):
	return 10

@my_dec
def my_func(a):
	a *= 80
	return a

print(my_func if type(my_func) == int else my_func(1))
print(type(my_func))

# ----------------------------------------------------
# №3

class A:
	def foo(self):
		print(10)

class B:
	def foo(self):
		print(1)

class C(A, B):
	pass

C().foo()

# ----------------------------------------------------
# №4
b = [1,2,3,4,1,2,1]

# a = [**{v for v in b}]
a = [k for k in {v for v in b}]
# a = [v for v in b if v not in a]
print(a)

# ----------------------------------------------------
# №5
a = 5
# a *= a
# a = a * a
a = a ** 2
print(a)
print('-' * 20)

# ----------------------------------------------------
# №6
a = 9
b = 2

print(a // b)

# ----------------------------------------------------
# №7
a = 9
b = 2

print(a % b)

# ----------------------------------------------------
# №8
name = 'John'
age = 30

print(f'Hello {name}, are you {age} years old?')
# ----------------------------------------------------
# №9
'''
При объявлении регулярного выражения в Python используется литера "r".
Это указывает на использование "сырых" строк (raw strings), в которых все символы,
включая слеши, интерпретируются буквально, без экранирования. Например, чтобы задать
регулярное выражение, которое ищет последовательность "ab", мы можем написать:
'''
pattern = r'ab'

'''
Использование сырых строк делает код более читабельным и понятным,
особенно если регулярное выражение содержит множество слешей.
'''

# ----------------------------------------------------
# №10
# print([x for x in [1, 2]])
print((x for x in [1, 2]))

# ----------------------------------------------------
# №10
# @

# ----------------------------------------------------
# №11
print(True * (False // True) == True - False)

# ----------------------------------------------------
# №12
class printer():
	def __init__(self):
		print('printer is on')

	def work(self):
		print(' '.join('printer goes brrrrrrrr'.split()[::-1]))

	def __del__(self):
		print('printer is off')

# printer.work() #TypeError: printer.work() missing 1 required positional argument: 'self'

print('-' * 20)
# ----------------------------------------------------
# №13
city = ['Moscow', 'Saint Pitersperg', 'Samara gorodok']

try:
	city = city.split()
except AttributeError:
	print(city[-1])
except:
	print(city[-1])
else:
	print(city[1] * 2)
finally:
	print(city[1::-1])

# ----------------------------------------------------
# №14
def sum1(lst):
	t = 0
	i = 0
	for e in lst:
		i += 1
		# print(e, type(e), type([]))
		if (type(e) == type([])):
			t = t + sum1(e)
		else:
			t = t + e + 2
	return t

print(sum1([1, 3, [2, 6, [5, 4]], 10]))

# ----------------------------------------------------
# №15
# Сортировка слиянием - сложность O(n log n)
# https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0_%D1%81%D0%BB%D0%B8%D1%8F%D0%BD%D0%B8%D0%B5%D0%BC
print('-' * 20)

# ----------------------------------------------------
# №16
# set
all_viruses = {'вирус 1', 'вирус 2', 'вирус 3', 'вирус 4', 'вирус 5'}
our_viruses = {'вирус 1', 'вирус 3', 'вирус 5'}

can_protect = our_viruses.intersection(all_viruses)
cannot_protect = all_viruses.difference(our_viruses)

print('Мы можем защитить от следующих вирусов:', can_protect)
print('Мы не можем защитить от следующих вирусов:', cannot_protect)

# ----------------------------------------------------
# №17
from math import sqrt
def dis(func):
	def inner(index):
		d = index[1] ** 2 - 4 * index[0] * index[2]
		func(index[0] * 2, -index[1], sqrt(d))
	return inner

@dis
def find_x(a, b, d):
	print((b + d) // a)

find_x([1, -2, -15])

# ----------------------------------------------------
# №18
class Triangle:
	def __init__(self, a, b ,c):
		self.__a = a
		self.__b = b
		self.__c = c

	def area(self):
		p = (self.__a + self.__b + self.__c) / 2
		return (p * (p - self.__a) * (p - self.__b) * (p - self.__c)) ** 0.5

tri = Triangle(3, 4, 5)
tri.__a = 2
print(int(tri.area()))

# ----------------------------------------------------
# №19
# open('result.txt', 'w').close()

# import os
# with open('result.txt', 'w'):
# 	os.utime('result.txt', None)

# open('result.txt').close() #FileNotFoundError: [Errno 2] No such file or directory: 'result.txt'

# from pathlib import Path
# Path('result.txt').touch()

# import os
# os.mknod('result.txt') #PermissionError: [Errno 1] Operation not permitted

# ----------------------------------------------------
# №20

import threading
import time

def worker(num):
	time.sleep(5 - num)
	print(num ** 2, end='')

t1 = threading.Thread(target=worker, args=(1,))
t2 = threading.Thread(target=worker, args=(2,))

t1.start()
t2.start()

t1.join()
t2.join()
