n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
norm = 0
for a_ele, b_ele in zip(a, b):
    c.append(a_ele-b_ele)
for a_ele, b_ele in zip(c, c):
    norm += a_ele*b_ele
print(norm)