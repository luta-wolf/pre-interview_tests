# a = []
# print(type(a))


# d = {0:1, 1:2, 2:3}
# print(sum(d))


# try:
# 	f = open('ss.txt')
# except IOError:
# 	print('Error')
# 	raise
# finally:
# 	print('finally')


# class Reti(object):
# 	def __init__(self, p, q):
# 		self.p = p
# 		self.q = q

# 	def __lt__(self, other):
# 		return self.p * other.q < other.p * self.q

# 	def __repr__(self):
# 		return "%d%d" % (self.p, self.q)

# a = [Reti(1, 2), Reti(3, 4), Reti(3, 5)]
# a.sort()
# print(a)


# s = '\nAlice\n'
# print(s.strip())

# a = 2J

# print(type(a))

# def gener():
# 	result = -1
# 	for i in range(1, 20):
# 		if i % 3 and i % 5 == 0:
# 			result = i
# 	return result

# def sett():
# 	a = gener()

# a = 5
# sett()
# print(a)


s = 'Alice'
print(sum(1 for c in s))
