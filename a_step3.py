n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = 0
for a_ele, b_ele in zip(a, b):
    c += a_ele*b_ele
print(c)
