import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import the Dataset
df = pd.read_excel('Data.xlsx')
df.head()
df.info()

plt.scatter(x=df['TotalOR1'], y=df['TotalOR2'])
plt.title('The Relationship between OR Rates')
plt.xlabel('OR Rate1')
plt.ylabel('OR Rate2')
plt.savefig('scatterplot.png')

print("Hello")

-- We don't want print statement here. Please Update this !!!
