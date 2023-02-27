new = input().replace("-", "").replace("(", "").replace(")", "").strip("+")
if len(new) == 11:
	new = new[1:]
if len(new) == 7:
    new = "495" + new
data = [input(), input(), input()]
for i in data:
    i = i.replace("-", "").replace("(", "").replace(")", "").strip("+")
    if len(i) == 1:
        i = i[1:]
    if len(i) == 7:
        i = "495" + i
    if new in i or i in new:
        print("YES")
    else:
        print("NO")

