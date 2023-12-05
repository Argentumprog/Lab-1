import pandas as pd
import matplotlib.pyplot as plt

test = pd.read_csv('test.csv')
test_sample = test.head(1000)

missed_values = test_sample.isnull().sum()
print(missed_values)

plt.boxplot(test_sample['Rooms'])
plt.show()

plt.figure()
plt.hist(test_sample['Rooms'])
plt.show()

mid_value = test_sample['Rooms'].mean()
test_sample['Rooms'].fillna(mid_value)


pivot_table = pd.pivot_table(test_sample, index='DistrictId', columns='Rooms', aggfunc='size', fill_value=0)
print(pivot_table)

test_sample.to_csv('Myresult.csv')