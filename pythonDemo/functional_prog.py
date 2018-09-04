# -×- coding:utf-8 -*-

# def add(x, y, f):
#     return f(1, x) + f(1, y)
#
#
# def f(n, x):
#     return n * x
#
#
# print(add(5, -6, f))


# def f(x):
#     return x ** 2
#
#
# r = map(f, [1, 2, 3, 4, 5, 6, 7])
# print(list(r))
#
# r1 = map(str, [1, 2, 3, 4, 5, 6])
# print(list(r1))

# from functools import reduce
#
#
# def fn(x, y):
#     return 10 * x + y
#
#
# def char2num(c):
#     return int(c)
#
#
# print(reduce(fn, map(char2num, ['1', '2', '3'])))

# def normalize(name):
#     name = name[0].upper() + name[1:].lower()
#     return name
#
#
# l1 = ['lmc', 'adaM', 'LISA']
# print(list(map(normalize, l1)))

# from functools import reduce
#
#
# def str2float(s):
#     def fn(x, y):
#         return 10 * x + y
#
#     def char2num(s):
#         digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#         return digit[s]
#
#     return reduce(fn, map(char2num, s.replace('.', '')))
#
#
# s = '1234.5678'
#
# if s.find('.') != -1:
#     print(str2float(s) / pow(10, (len(s) - s.find('.') - 1)))
# else:
#     print(str2float(s))

# def is_palindrome(n):
#     s1 = str(n)
#     s2 = s1[::-1]
#
#     if s1 == s2:
#         return True
#     else:
#         return False
# l = [1, 909, 12321, 2134]
# print(list(filter(is_palindrome, l)))

def by_name(t):
    # return t[0].lower()
    return t[1]


l = [('Dob', 75), ('Adam', 92), ('Bart', 66), ('cisa', 88)]
l1 = {'Dob': 75, 'Adam': 92, 'Bart': 66, 'cisa': 88}
l_sort = sorted(l, key=by_name)
print(l_sort)





