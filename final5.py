import numpy as np
import matplotlib.pyplot as plt

histogram_data = {
    100: 12, 101: 18, 102: 32, 103: 48, 104: 52, 105: 65, 106: 55, 107: 42, 108: 32, 109: 16,
    110: 10, 140: 5, 141: 18, 142: 25, 143: 32, 144: 40, 145: 65, 146: 43, 147: 32, 148: 20,
    149: 10, 150: 4
}

histogram = np.zeros(256)
for intensity, count in histogram_data.items():
    histogram[intensity] = count

def otsu_threshold(histogram):
    total = sum(histogram)
    sumB = 0.0
    wB = 0
    maximum = 0.0
    sum1 = np.dot(np.arange(len(histogram)), histogram)
    for i in range(len(histogram)):
        wB += histogram[i]
        if wB == 0:
            continue
        wF = total - wB
        if wF == 0:
            break
        sumB += i * histogram[i]
        mB = sumB / wB
        mF = (sum1 - sumB) / wF
        between = wB * wF * ((mB - mF) ** 2)
        if between > maximum:
            best_idx = i
            maximum = between

    return best_idx

threshold = otsu_threshold(histogram)
print("En uygun eşik değeri:", threshold)

plt.bar(np.arange(len(histogram)), histogram, color='gray')
plt.axvline(x=threshold, color='red', linestyle='--')
plt.title("Histogram ve Otsu Eşik Değeri")
plt.xlabel("Yoğunluk Değeri")
plt.ylabel("Piksel Sayısı")
plt.show()