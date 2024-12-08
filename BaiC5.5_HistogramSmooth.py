def histo_smooth(n, his, w):
    re = []

    for i in range(n):
        start = max(0, i - w // 2)
        end = min(n, i + w // 2 + 1)

        aver = sum(his[start:end]) / (end - start)
        re.append(int(round(aver)))
    return re


data = input().strip()
while len(data) == 0:
    data = input().strip()

n = int(data)
histogram = []


smooth_w3 = histo_smooth(n, histogram, 3)
smooth_w5 = histo_smooth(n, histogram, 5)

print("Smoothed Histogram w=3")
print(" ".join(map(str, smooth_w3)))

print("Smoothed Histogram w=5")
print(" ".join(map(str, smooth_w5)))
