import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import pandas as pd

# Random floating-point data
data = np.random.uniform(0.0, 100.0, (10, 2))
np.set_printoptions(precision=4)
print(data)

# Transform the data
scaler_model = MinMaxScaler()
scaler_model.fit(data)
data = scaler_model.transform(data)
print(data)

mydata = np.random.uniform(0, 101, (50,4))
df = pd.DataFrame(data=mydata, columns=['f1', 'f2', 'f3', 'label'])

# Splitting data for test data
x = df[['f1', 'f2', 'f3']]
y = df['label']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
print(x_train.shape)
print(x_test.shape)
