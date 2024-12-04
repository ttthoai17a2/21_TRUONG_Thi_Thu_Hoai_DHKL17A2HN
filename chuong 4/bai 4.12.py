import pandas as pd
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

df_vertical = pd.concat([ser1, ser2], axis=0, ignore_index=True)
df_horizontal = pd.concat([ser1, ser2], axis=1)

print("Xếp chồng theo chiều dọc:")
print(df_vertical)

print("\nXếp chồng theo chiều ngang:")
print(df_horizontal)
