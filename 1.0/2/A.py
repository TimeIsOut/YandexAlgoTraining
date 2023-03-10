data = list(map(int, input().split()))
for i in range(len(data) - 1):
    if data[i] >= data[i + 1]:
        print("NO")
        break
else:
    print("YES")
