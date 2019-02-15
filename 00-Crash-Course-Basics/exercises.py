# ** Import numpy,pandas,matplotlib,and sklearn. Also set visualizations to be shown inline in the notebook.**
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# ** Set Numpy's Random Seed to 101 **
np.random.seed(101)

# ** Create a NumPy Matrix of 100 rows by 5 columns consisting of random integers from 1-100. (Keep in mind that the upper limit may be exclusive.**
mat = np.random.randint(1, 101, (100, 5))

# ** Create a 2-D visualization using plt.imshow of the numpy matrix with a colorbar.
# Add a title to your plot.
# Bonus: Figure out how to change the [*aspect*](https://stackoverflow.com/questions/10540929/figure-of-imshow-is-too-small) of the imshow() plot. **
plt.imshow(mat, aspect=0.05)
plt.title("TITLE")
plt.colorbar()
plt.show()

# ** Now use pd.DataFrame() to read in this numpy array as a dataframe.
# Simple pass in the numpy array into that function to get back a dataframe.
# Pandas will auto label the columns to 0-4**
df = pd.DataFrame(mat)

# ** Now create a scatter plot using pandas of the 0 column vs the 1 column. **
df.plot(x=0, y=1, kind='scatter')
plt.show()

# ** Now scale the data to have a minimum of 0 and a maximum value of 1 using scikit-learn. **
scaler_model = MinMaxScaler()
scaled_data = scaler_model.fit_transform(df)

# ** Using your previously created DataFrame, 
# use [df.columns = [...]](https://stackoverflow.com/questions/11346283/renaming-columns-in-pandas) to rename
# the pandas columns to be ['f1','f2','f3','f4','label']. Then perform a train/test split with scikitlearn.**
df.columns = ['f1', 'f2', 'f3', 'f4', 'label']
x = df[['f1', 'f2', 'f3', 'f4']]
y = df['label']
x_train, x_test, y_train, y_test = train_test_split(x, y)
