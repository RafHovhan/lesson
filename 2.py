a = int(input())

for i in range(0, a+1):
    g = (i + i) + ((i + i) * 2)
    if g == a:
        P = i
        s = i
        K = (i + i) * 2
        print(f"{P} {K} {s}")