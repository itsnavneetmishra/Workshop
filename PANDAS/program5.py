# This is program5.py


import pandas as pd


dataframe = pd.DataFrame({'id ' : [7058,4511,7014,7033],
                         'name' :  ['Navneet','Shivam','yash','sarthak'],
                         "maths_marks" : [99,97,98,90],
                         "physics_marks" : [99,98,97,96] }

                         )

#display dataframe

print(dataframe)

"""print("--------------------------------------------")

print(dataframe.describe())

print("--------------------------------------------")

print(dataframe['maths_marks'].unique())

print("--------------------------------------------")

print(dataframe['maths_marks'].nunique())


print("--------------------------------------------")


print(dataframe.columns)

print(dataframe.info())

print("--------------------------------------------")"""

print(dataframe.min())


print()


print(dataframe.max())

print(dataframe.sum())

print(dataframe.count())


print(dataframe.groupby('name').first())



print(dataframe.groupby('name')['physics_marks'].sum())



print(dataframe.groupby('name')['maths_marks'])
