import pandas as pd
import numpy as np

truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)

mse = ((truth - pred) ** 2).mean()
print(f"Sai số bình phương trung bình (MSE): {mse}")
