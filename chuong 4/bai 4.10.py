import pandas as pd
import numpy as np

ser = pd.Series(np.random.randint(1, 10, 7))
indices = ser[ser % 3 == 0].index

print("Chuỗi dữ liệu:")
print(ser)
print("\nVị trí của các số là bội của 3:")
print(indices)
