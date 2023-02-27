troom, tcond = map(int, input().split())
mode = input()
if mode == "heat" and troom <= tcond:
	print(tcond)
elif mode == "freeze" and troom >= tcond:
	print(tcond)
elif mode == "auto":
	print(tcond)
else:
	print(troom)

