a = list(map(int, input().split()))
b = list(map(int, input().split()))
dotPro = 0
for a_ele, b_ele in zip(a, b):
    dotPro += a_ele*b_ele
if(dotPro == 0):
    print("Yes")
else:
    print("No")