# 1: Đọc dữ liệu từ tệp CSV
import pandas as pd
drinks = pd.read_csv('drinks.csv', index_col=0)

print("Type of 'drinks':", type(drinks))
print("Shape of 'drinks':", drinks.shape)
print("Columns in 'drinks':", drinks.columns)
print("\nFirst 5 rows of 'drinks':")
print(drinks.head())
print("\nLast 5 rows of 'drinks':")
print(drinks.tail())

#2.Số lượng bia tiêu thụ trung bình ở mỗi châu lục
average_beer_consumption = drinks.groupby('continent')['beer_servings'].mean()
print("Average beer consumption by continent:")
print(average_beer_consumption)

#3.Thống kê tổng quát về số lượng rượu vang tiêu thụ ở mỗi châu lục
wine_consumption_stats = drinks.groupby('continent')['wine_servings'].describe()
print("Wine consumption statistics by continent:")
print(wine_consumption_stats)

#4.Số lượng bia và rượu tiêu thụ trung bình ở mỗi châu lục
average_consumption = drinks.groupby('continent')[['beer_servings', 'wine_servings']].mean()
print("Average beer and wine consumption by continent:")
print(average_consumption)

#5.Giá trị trung vị (median) cho các loại bia và rượu tiêu thụ ở mỗi châu lục
median_consumption = drinks.groupby('continent')[['beer_servings', 'wine_servings']].median()
print("Median beer and wine consumption by continent:")
print(median_consumption)

#6.Số lượng rượu mạnh (spirit_servings) tiêu thụ trung bình, lớn nhất và nhỏ nhất ở mỗi châu lục
spirit_servings_stats = drinks.groupby('continent')['spirit_servings'].agg(['mean', 'max', 'min'])
print("Spirit servings stats by continent:")
print(spirit_servings_stats)

#7.Sắp xếp dữ liệu theo số lượng bia tiêu thụ và hiển thị các quốc gia tiêu thụ bia nhiều nhất và ít nhất

       # Sắp xếp dữ liệu theo số lượng bia tiêu thụ
sorted_by_beer = drinks.sort_values(by='beer_servings', ascending=False)

       # Hiển thị 5 quốc gia có lượng tiêu thụ bia nhiều nhất
print("Top 5 countries with highest beer consumption:")
print(sorted_by_beer.head())

       # Hiển thị 5 quốc gia có lượng tiêu thụ bia ít nhất
print("Top 5 countries with lowest beer consumption:")
print(sorted_by_beer.tail())
