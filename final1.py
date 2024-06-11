import pandas as pd
import numpy as np

data_path = '/mnt/data/soru1_2_data.csv'
image_data = pd.read_csv(data_path, header=None)

pixels = image_data.to_numpy()

L = 256

min_pixel = pixels.min()
max_pixel = pixels.max()

new_pixels = (pixels - min_pixel) / (max_pixel - min_pixel) * (L - 1)