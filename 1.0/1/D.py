a, b, c = int(input()), int(input()), int(input())
if a == b == c == 0:
    print("MANY SOLUTIONS")
elif c < 0 or a == b == 0:
    print("NO SOLUTION")
elif a == 0:
    if b == c * c:
        print("MANY SOLUTIONS")
    else:
        print("NO SOLUTION")
else:
    if (c * c - b) / a == int((c * c - b) / a):
        print(int((c * c - b) / a))
    else:
        print("NO SOLUTION")

