import numpy as np
import pandas as pd
ages = np.array([15, 15, 16, 19, 19, 20, 20, 21, 22, 28, 35, 40, 41, 42, 43, 44, 60, 61, 65]) #Dosyada Verilen Yaş Değerleri
c1,c2 = 16,22
dfs = [] #Sonuçları göstermek için liste - DataFrame
for iteration in range(4):
  distance1 = np.abs(ages - c1)
  distance2 = np.abs(ages - c2)
  nearest_cluster = np.where(distance1 < distance2,1,2) # en yakın kümeyi seçiyoruz

  c1_new = np.mean(ages[nearest_cluster == 1])
  c2_new = np.mean(ages[nearest_cluster == 2])
  df = pd.DataFrame({
      'xi': ages,
      'c1': np.full(ages.shape, c1),
      'c2': np.full(ages.shape, c2),
      'Distance1': distance1,
      'Distance2': distance2,
      'Nearest Cluster': nearest_cluster,
      'New Centroid c1': np.full(ages.shape, c1_new),
      'New Centroid c2': np.full(ages.shape, c2_new)
  })
  dfs.append(df)

c1,c2 = c1_new,c2_new
all_iterations_df = pd.concat(dfs, keys=range(1, len(dfs) + 1), names=['Iteration'])
pd.options.display.max_rows = None # belirli bir sayıdan sonra değerler göstermeme durumunu yok sayar
pd.DataFrame(all_iterations_df)

print(pd.DataFrame(all_iterations_df))