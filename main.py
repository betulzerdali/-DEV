import numpy as np
import matplotlib.pyplot as plt
import random
import math

g = 10  # yer çekimi ivmesi
angle = math.radians(30)
h = 7  # okul numaramın son 2 hanesi 07
min_v = 330  # minimum hız
max_v = 1800  # maximum hız

v_0 = (min_v + max_v) / 2  # hız

# Hesaplama Bilgileri
d_distance = 20000 + 200 * random.randint(-10, 10)  # uzaklık mesafesi
width_start = d_distance  # genişlik_baslangıc=uzaklık_mesafesi
width_end = d_distance + 1000 + 100 * random.randint(-2, 2)  # genişlik bitiş


def shot_calculation(vx, vy, h):
    t_exit = vy / g
    t_down = np.sqrt(vy ** 2 + 2 * g * h) / g
    t_air = t_exit + t_down

    x_range = vx * t_air
    return t_air, x_range


def shoot(min_v, max_v, width_start, width_end):
    shoot_num = 0
    x_values = []
    y_values = []

    while True:
        v_avg = (min_v + max_v) / 2  # ortalama hız
        vx = v_avg * np.cos(angle)
        vy = v_avg * np.sin(angle)

        t_air, x_range = shot_calculation(vx, vy, h)

        shoot_num += 1

        if x_range < width_start:
            min_v = v_avg
            print("önüne düştü")
        elif x_range > width_end:
            max_v = v_avg
            print("uzakına düştü")
        else:
            print(f"{shoot_num}. seferde vuruş gerçekleşmiştir. Hedefi vurmak için gerekli hız {v_avg} km/s'dir")
            
            # veriler
            t_values = np.linspace(0, t_air, 1000)
            x_values = vx * t_values
            y_values = h + vy * t_values - 0.5 * g * t_values ** 2
            
            break
    
    # grafik çizimi
    plt.plot(x_values, y_values)
    plt.xlabel('Mesafe (metre)')
    plt.ylabel('Yükseklik (metre)')
    plt.title('deneme sayısı: {}'.format(shoot_num))
    plt.show()

shoot(min_v, max_v, width_start, width_end)
