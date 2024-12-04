import pandas as pd
euro12 = pd.read_csv('euro12.csv')

print(euro12.info())
print("Shape of euro12:", euro12.shape)
print("Columns in euro12:", euro12.columns)

# 1.In giá trị cột 'Goals'
print(euro12['Goals'])

# 2.Số đội tham gia Euro 2012
print("Number of teams in Euro 2012:", euro12['Team'].nunique())

#3. In thông tin của DataFrame euro12
print(euro12)

#4. Tạo DataFrame discipline với các cột 'Team', 'Yellow Cards', 'Red Cards'
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print(discipline)

# 5.Sắp xếp discipline giảm dần theo 2 cột 'Red Cards', 'Yellow Cards'
discipline_sorted = discipline.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=False)
print(discipline_sorted)

# 6.Tính trung bình của 'Yellow Cards'
print("Average Yellow Cards:", euro12['Yellow Cards'].mean())

# Lọc các đội có số bàn thắng (Goals) lớn hơn 6
teams_above_6_goals = euro12[euro12['Goals'] > 6]
print(teams_above_6_goals)

#7.In các đội mà tên bắt đầu bằng 'G'
teams_start_with_G = euro12[euro12['Team'].str.startswith('G')]
print(teams_start_with_G)

# 8.In 7 cột đầu của euro12
print(euro12.iloc[:, :7])

#9. In tất cả các cột, trừ 3 cột cuối
print(euro12.iloc[:, :-3])

#10.In các cột 'Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards'
print(euro12[['Team', 'Goals', 'Shooting Accuracy', 'Yellow Cards', 'Red Cards']])

# 11.In các cột chỉ hiển thị 'Team', 'Shooting Accuracy' từ 'England', 'Italy', 'Russia'
selected_teams = euro12[euro12['Team'].isin(['England', 'Italy', 'Russia'])][['Team', 'Shooting Accuracy']]
print(selected_teams)




