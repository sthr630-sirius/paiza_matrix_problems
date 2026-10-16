n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for a_ele, b_ele in zip(a, b):
    c.append(a_ele-b_ele)
print(*c)