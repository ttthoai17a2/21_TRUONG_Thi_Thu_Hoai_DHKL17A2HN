import pandas as pd

ser = pd.Series(['how', 'to', 'kick', 'ass?'])
ser_capitalized = ser.str.capitalize()

print("Chuỗi sau khi chuyển ký tự đầu tiên thành chữ hoa:")
print(ser_capitalized)
