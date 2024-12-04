'''
1.ser.values.reshape(7, 5):
        Chuyển Series thành mảng NumPy (ser.values) và định hình lại thành mảng có 7 hàng, 5 cột.
2. pd.DataFrame():
        Chuyển mảng định hình lại thành DataFrame.
3.columns=[f"Col{i+1}" for i in range(5)]:
        Tạo tên cột tự động cho DataFrame, ví dụ: "Col1", "Col2", ...
4.Kết quả:
df là một DataFrame có kích thước 7x5, với dữ liệu từ chuỗi ban đầu.
'''

import pandas as pd
import numpy as np

ser = pd.Series(np.random.randint(1, 10, 35))

df = pd.DataFrame(ser.values.reshape(7, 5), columns=[f"Col{i+1}" for i in range(5)])

print("Chuỗi dữ liệu ban đầu:")
print(ser)
print("\nDataFrame sau khi định hình lại:")
print(df)
