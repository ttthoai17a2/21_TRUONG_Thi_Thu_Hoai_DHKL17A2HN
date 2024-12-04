import pandas as pd

ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))

pos = [0, 4, 8, 14, 20]

extracted_values = ser.iloc[pos]

print("Chuỗi dữ liệu ban đầu:")
print(ser)
print("\nCác mục tại các vị trí trong danh sách pos:")
print(extracted_values)
