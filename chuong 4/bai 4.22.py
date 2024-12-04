import pandas as pd

# Đọc tệp stocks1.csv
stocks1 = pd.read_csv('stocks1.csv')

# Hiển thị 5 dòng đầu và cuối của stocks1
print("First 5 rows of stocks1:")
print(stocks1.head())
print("\nLast 5 rows of stocks1:")
print(stocks1.tail())

# Hiển thị kiểu dữ liệu (dtype) của các cột của stocks1
print("\nData types of columns in stocks1:")
print(stocks1.dtypes)

# Hiển thị thông tin (info) của stocks1
print("\nInfo of stocks1:")
print(stocks1.info())
##########################################################1
# Đọc tệp stocks2.csv
stocks2 = pd.read_csv('stocks2.csv')

# Hiển thị 5 dòng đầu và cuối của stocks2
print("First 5 rows of stocks2:")
print(stocks2.head())
print("\nLast 5 rows of stocks2:")
print(stocks2.tail())

# Hiển thị kiểu dữ liệu (dtype) của các cột của stocks2
print("\nData types of columns in stocks2:")
print(stocks2.dtypes)

# Hiển thị thông tin (info) của stocks2
print("\nInfo of stocks2:")
print(stocks2.info())
########################################################2
# Đọc tệp companies.csv
companies = pd.read_csv('companies.csv')

# Hiển thị dữ liệu của companies
print("Data of companies:")
print(companies)

# Hiển thị kiểu dữ liệu (dtype) của các cột của companies
print("\nData types of columns in companies:")
print(companies.dtypes)

# Hiển thị thông tin (info) của companies
print("\nInfo of companies:")
print(companies.info())
######################################################3
# Kiểm tra nếu có dữ liệu Null trong stocks1
print("\nCheck for null values in stocks1:")
print(stocks1.isnull().sum())

# Thay thế dữ liệu Null
stocks1['high'] = stocks1['high'].fillna(stocks1.groupby('symbol')['high'].transform('max'))
stocks1['low'] = stocks1['low'].fillna(stocks1.groupby('symbol')['low'].transform('min'))

print("\nCheck for null values after replacement in stocks1:")
print(stocks1.isnull().sum())

######################################################

# Gộp stocks1 và stocks2 theo dòng
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

# Hiển thị 15 dòng dữ liệu cuối của stocks
print("\nLast 15 rows of the combined stocks dataframe:")
print(stocks.tail(15))


##################################################
# Gộp stocks và companies theo cột 'symbol' để tạo stocks_companies
stocks_companies = pd.merge(stocks, companies, left_on='symbol', right_on='name', how='left')

# Hiển thị 5 dòng dữ liệu đầu của stocks_companies
print("\nFirst 5 rows of the stocks_companies dataframe:")
print(stocks_companies.head())

#############################################
# Tính giá (open, high, low, close) trung bình và volume trung bình của mỗi công ty
avg_price_and_volume = stocks_companies.groupby('symbol')[['open', 'high', 'low', 'close', 'volume']].mean()
print("\nAverage open, high, low, close, and volume for each company:")
print(avg_price_and_volume)

#########################################333
# Tính giá đóng cửa (close) trung bình, lớn nhất và nhỏ nhất của mỗi công ty
close_stats = stocks_companies.groupby('symbol')['close'].agg(['mean', 'max', 'min'])
print("\nAverage, max, and min close price for each company:")
print(close_stats)

#############################################33

# Tạo cột parsed_time bằng cách chuyển đổi cột 'date' sang định dạng DateTime
stocks_companies['parsed_time'] = pd.to_datetime(stocks_companies['date'])

# Hiển thị kiểu dữ liệu của cột parsed_time
print("\nData type of 'parsed_time':")
print(stocks_companies['parsed_time'].dtype)

# Hiển thị 5 dòng đầu của stocks_companies với cột parsed_time
print("\nFirst 5 rows of stocks_companies with parsed_time:")
print(stocks_companies.head())

##################################3
# Thêm cột result
stocks_companies['result'] = ['up' if close > open else 'down' for close, open in zip(stocks_companies['close'], stocks_companies['open'])]

# Hiển thị 5 dòng đầu của stocks_companies với cột result
print("\nFirst 5 rows of stocks_companies with 'result' column:")
print(stocks_companies.head())
