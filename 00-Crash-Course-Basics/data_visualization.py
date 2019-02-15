import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("")

# Graphical plot
x = np.arange(0, 10)
print(x)
y = x**2
plt.plot(x, y, 'r--')
plt.xlim(0,4)
plt.ylim(0,10)
plt.title("TITLE")
plt.xlabel("X LABEL")
plt.ylabel("Y LABEL")
plt.show()

# Image show using 2D gradient
mat = np.arange(0, 100).reshape(10, 10)
plt.imshow(mat, cmap='coolwarm')
plt.colorbar()
plt.show()

# Using pandas to do a scatter plot
df = pd.read_csv("./00-Crash-Course-Basics/salaries.csv")
df.plot(x='Salary', y='Age', kind='scatter')
plt.show()
