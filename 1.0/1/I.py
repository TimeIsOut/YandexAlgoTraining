A, B, C, D, E = int(input()), int(input()), int(input()), int(input()), int(input())
minn, maxx = min(A, B, C), max(A, B, C)
avg = A + B + C - minn - maxx
w, h = min(D, E), max(D, E)
if w >= minn and h >= avg:
    print("YES")
else:
    print("NO")