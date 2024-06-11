import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = '/content/soru3_data.csv'
image_data = pd.read_csv(file_path, header=None)

kernel = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
]) / 16

def apply_gaussian_filter(image, kernel):
    kernel_size = kernel.shape[0]
    offset = kernel_size // 2
    filtered_image = np.zeros((image.shape[0] - 2*offset, image.shape[1] - 2*offset))
    
    for i in range(offset, image.shape[0] - offset):
        for j in range(offset, image.shape[1] - offset):
            region = image[i-offset:i+offset+1, j-offset:j+offset+1]
            filtered_value = np.sum(region * kernel)
            filtered_image[i-offset, j-offset] = filtered_value
    
    return filtered_image

image_array = image_data.values

filtered_image = apply_gaussian_filter(image_array, kernel)

plt.figure(figsize=(8, 8))
plt.imshow(filtered_image, cmap='gray')
plt.title('Gauss Yumuşatma Filtresi Uygulanmış Görüntü')
plt.colorbar()
plt.show()