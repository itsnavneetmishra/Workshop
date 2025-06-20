import pandas as pd


d={'one':pd.Series([100,200,300],index=['apple','ball','clock']),'two':pd.Series([10,12,14,16],index=['apple','bat','ball','cat'])}
df = pd.DataFrame(d) #DF=data structure of pandas
print(df)

################################
print("index")
print(df.index)

################################
print("columns")
print(df.columns)

#################################
print("specific")
print(pd.DataFrame(d,['apple','ball','cat']))

#################################






