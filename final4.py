data = {
    100: 12, 101: 18, 102: 32, 103: 48, 104: 52, 105: 65, 106: 55,
    107: 42, 108: 32, 109: 16, 110: 10, 140: 5, 141: 18, 142: 25,
    143: 32, 144: 40, 145: 65, 146: 43, 147: 32, 148: 20, 149: 10, 150: 4
}

def calculate_threshold(data, initial_threshold=100, threshold=1):
    T0 = initial_threshold
    while True:
        G1 = [intensity for intensity, count in data.items() if intensity > T0]
        G2 = [intensity for intensity, count in data.items() if intensity <= T0]
        
        m1 = sum(intensity * data[intensity] for intensity in G1) / sum(data[intensity] for intensity in G1)
        m2 = sum(intensity * data[intensity] for intensity in G2) / sum(data[intensity] for intensity in G2)
        
        T1 = (m1 + m2) / 2
        
        if abs(T1 - T0) <= threshold:
            return T1
        
        T0 = T1

optimal_threshold = calculate_threshold(data)
print(f"Optimal Eşik Değeri: {optimal_threshold}") 