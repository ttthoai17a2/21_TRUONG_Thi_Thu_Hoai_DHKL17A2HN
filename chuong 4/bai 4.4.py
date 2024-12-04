#### 1

import pandas as pd

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

ser1_filtered = ser1[~ser1.isin(ser2)]

print("Kết quả sau khi xóa các mục có trong ser2:")
print(ser1_filtered)




#####2

# Lấy tất cả các mục của ser1 và ser2 nhưng không nằm chung trong cả hai
khac_biet_doi_xung = pd.Series(list(set(ser1).symmetric_difference(set(ser2))))

print("\nKết quả các mục không nằm chung trong cả hai:")
print(khac_biet_doi_xung)
