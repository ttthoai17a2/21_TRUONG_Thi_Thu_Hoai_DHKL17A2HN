import pandas as pd
import numpy as np

fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))

average_weights = weights.groupby(fruit).mean()

print("Khối lượng trung bình của từng loại quả:")
print(average_weights)
