
import math as mt

# вершины пронумированы от 1 до n включительно

n = 0
d = [0, 0] # у нулевой вершины (ее нет) глубина - 0. у первой вершины (она корень) глубина - 0
parent = [0, 0] # у нулевой вершины (ее нет) предок - 0. у первой вершины (она корень) предок - 0
jmp = [[], []]

def build_jmp_for(v):
    jmp[v].append(parent[v])
    for k in range(1, round(mt.log2(n))+1):
        jmp[v].append(jmp[jmp[v][k-1]][k-1])

def LCA(u, v):
    if d[u] < d[v]:
        return LCA(v, u)

    for k in range(round(mt.log2(n)), -1, -1):
        u1 = jmp[u][k]
        if d[u1] >= d[v]:
            u = u1

    if u == v:
        return u

    for k in range(round(mt.log2(n)), -1, -1):
        u1 = jmp[u][k]
        v1 = jmp[v][k]
        if u1 != v1:
            u = u1
            v = v1

    assert parent[u] == parent[v], 'parent[u] != parent[v]'

    return parent[u]


n = int(input())

kids = []        # у листьев будет 0

for i in range(n+1):
    kids.append([])

for i in range(2, n+1):
    p = int(input())
    parent.append(p)

    kids[p].append(i)

    jmp.append([]) # для каждой вершины резервируем масив прыжков
    d.append(0)  # для каждой вершины нитим глубину

for k in range(1, round(mt.log2(n)) + 1): # сразу проинитим jmp нлевой, те несуществующей вершины и первой, те корня
    jmp[0].append(0)
    jmp[1].append(1)

# print(parent)
# print("========================")
# print(kids)
# print("========================")

# DFS
stack = [1]
while len(stack) != 0:
    v = stack.pop()
    # for i in range(len(parent)):
    #     if parent[i] == v:
    #         stack.append(i)

    stack.extend(kids[v])

    if parent[v] != 0:
        d[v] = d[parent[v]] + 1
        build_jmp_for(v)

# print(d)
# print("========================")
# print(jmp)
# print("========================")

m = int(input())
for j in range(m):
    [u, v] = map(int, input().split())
    print(LCA(u, v))




# stack = [1]
# while len(stack) != 0:
#     v = stack.pop()
#     stack.extend(kids[v])
#
#     if parent[v] != 0:
#         d[v] = d[parent[v]] + 1




