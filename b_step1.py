import numpy as np
h, w = map(int, input().split())

a = np.array(list(map(int, input().split())))
for _ in range(h-1):
    c = list(map(int, input().split()))
    a = np.vstack((a, c))

b = np.array(list(map(int, input().split())))
for _ in range(h-1):
    c = list(map(int, input().split()))
    b = np.vstack((b, c))

if(h == 1):
    print(*a+b)
else:
    for l in a+b:
        print(*l)