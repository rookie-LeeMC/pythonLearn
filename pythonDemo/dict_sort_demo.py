# -*-coding:utf-8 -*-

# 通过key值排序
# 方法一
# l = {'Dob': 75, 'Adam': 92, 'Bart': 66, 'Cisa': 88}
# sort_key_list = sorted(l.keys())
# print(l)
#
# sorted_list = map(lambda x: {x: l[x]}, sort_key_list)
# print(list(sorted_list))
# # 方法二
# ll = sorted(l.items(), key=lambda item: item[0])
# print(ll)

# 通过value值排序
l = {'Dob': 75, 'Adam': 92, 'Bart': 66, 'Cisa': 88}
sort_key_list = sorted(l, key=lambda x: l[x])
print(sort_key_list)

sorted_list = map(lambda x: {x: l[x]}, sort_key_list)
print(list(sorted_list))
