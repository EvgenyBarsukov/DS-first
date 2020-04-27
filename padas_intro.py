import pandas as pd
import numpy as np

students_performance = pd.read_csv('StudentsPerformance.csv')
titanic = pd.read_csv('titanic.csv')
# print(students_performance.head())
# print(students_performance.head(1))
# print(students_performance.tail(1))
# print(students_performance.describe())
# print(students_performance.dtypes)
# print(students_performance.shape)
# print(students_performance.groupby('gender').aggregate({'writing score': 'mean'}))
# print(students_performance.size)


# first 5 observation and first 3 variables
# print(students_performance.iloc[0:5, 0:3])
# print(students_performance.iloc[[0, 3, 6], 0:3])

# with_names = students_performance.iloc[[0, 3, 4, 7, 8]]
# with_names.index = ['Cersei', 'Tywin', 'Gregor', 'Joffrey', 'Ilyn Payne']
# print(with_names)
# print(with_names.loc[['Cersei', 'Joffrey'], ['gender', 'writing score']])

# print(with_names.iloc[:, 0])
# print(type(with_names.iloc[:, 0]))

# print(pd.Series([1, 2, 3], index=['Cersei', 'Tywin', 'Gregor'] ))
# my_series1 = pd.Series([1, 2, 3], index=['Cersei', 'Tywin', 'Gregor'])
# my_series2 = pd.Series([4, 5, 6], index=['Cersei', 'Tywin', 'Gregor'])
# print(pd.DataFrame({'col_name1': my_series1, 'col_name2': my_series2}))

# print(with_names['gender'])
# print(with_names[['gender']])
# print(with_names['gender'].shape)
# print(with_names[['gender']].shape)

print(titanic.shape)
print(titanic.dtypes.value_counts())