import pandas as pd

ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])
diff1 = ser.diff()

diff2 = diff1.diff()

print("Hiệu số của các phần tử liên tiếp:")
print(diff1)
print("\nHiệu số của hiệu số giữa các số liên tiếp:")
print(diff2)
