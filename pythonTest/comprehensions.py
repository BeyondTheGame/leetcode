# 大小写key合并
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
    # if k.lower() in ['a', 'b']
}
print(mcase_frequency)


# 快速互换key和value
mcase = {'a': 10, 'b': 34}
mcase_frequency = {v: k for k, v in mcase.items()}
print(mcase_frequency)


# 集合推到式
squared = {x**2 for x in [1, 1, 2]}
print(squared)
print('-----------------------------------')
alist = list(map(lambda x: x*x, range(10)))
print(alist)

# 使用列表推导式实现嵌套列表的平铺
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
alist = [num for ele in vec for num in ele]
print(alist)

scores = {"zhang shan": 45, "li si": 78, "wang wu": 40}
highest = max(scores.values())
highPersonName = [name for name, value in scores.items() if value == highest]
print(highPersonName)

print('-----------------------------------')
# 实现多序列元素的任意组合
alist = [(x, y) for x in (1, 2, 3) for y in (3, 1, 4) if x != y]
print(alist)

print('----------实现矩阵转置----------------')
# 实现矩阵转置
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
maxtrixT = [[row[i] for row in matrix] for i in range(4)]
print(maxtrixT)
a = list(zip(*matrix))
print(list(map(list, a)))

print('----------列表推导式生成 100 以内的素数----------------')
import math
alist = [p for p in range(2, 100) if 0 not in [p % d for d in range(2, int(math.sqrt(p))+1)] ]
print(alist)