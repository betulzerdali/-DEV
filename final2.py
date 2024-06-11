import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    return pd.read_csv(file_path, header=None)

def calculate_histogram(data):
    hist, _ = np.histogram(data, bins=np.arange(257))
    return hist

def calculate_cdf(hist):
    cdf = np.cumsum(hist)
    cdf_min = cdf[np.nonzero(cdf)].min()
    return cdf, cdf_min

def histogram_equalization(data):
    hist = calculate_histogram(data)
    cdf, cdf_min = calculate_cdf(hist)
    cdf_normalized = (cdf - cdf_min) * 255 / (data.size - cdf_min)
    cdf_normalized = np.round(cdf_normalized).astype('uint8')
    equalized_image = cdf_normalized[data]
    return equalized_image, hist, cdf

file_path = '/content/soru1_2_data.csv'

image_data = load_data(file_path)

equalized_image, hist, cdf = histogram_equalization(image_data.values)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].bar(np.arange(256), hist, color='gray')
axs[0, 0].set_title("Original Histogram")

new_hist = calculate_histogram(equalized_image)
axs[0, 1].bar(np.arange(256), new_hist, color='gray')
axs[0, 1].set_title("Equalized Histogram")

axs[1, 0].imshow(image_data, cmap='gray')
axs[1, 0].set_title("Original Image")

axs[1, 1].imshow(equalized_image, cmap='gray')
axs[1, 1].set_title("Equalized Image")

plt.tight_layout()
plt.show()