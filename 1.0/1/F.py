w1, h1, w2, h2 = map(int, input().split())
cm1, cm2 = 0, 0
mw, mh = max(w1, w2), max(h1, h2)
if (h1 + h2) * mw <= (w1 + w2) * mh:
    cm1, cm2 = h1 + h2, mw
else:
    cm1, cm2 = w1 + w2, mh
w2, h2 = h2, w2
mw, mh = max(w1, w2), max(h1, h2)
if (h1 + h2) * mw <= (w1 + w2) * mh:
    cm3, cm4 = h1 + h2, mw
else:
    cm3, cm4 = w1 + w2, mh
if cm1 * cm2 >= cm3 * cm4:
    print(cm3, cm4)
else:
    print(cm1, cm2)