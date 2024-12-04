import pandas as pd
import numpy as np

np.random.seed(100)  
ser = pd.Series(np.random.randint(1, 5, [12]))

value_counts = ser.value_counts()

top_2 = value_counts.index[:2]

ser_replaced = ser.where(ser.isin(top_2), 'Other')

print("Chuỗi ban đầu:")
print(ser)

print("\nChuỗi sau khi thay thế:")
print(ser_replaced)
