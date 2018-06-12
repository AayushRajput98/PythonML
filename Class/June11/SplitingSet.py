from sklearn.cross_validation import train_test_split
import pandas as pd
df=pd.read_excel("c:\\users\\lenovo\\documents\\Data.xlsx","Sheet1")
df=pd.DataFrame(df)
x, y = df.iloc[:,1:4].values,df.iloc[:,0].values
x_train, x_test, y_train, y_test=train_test_split(x, y, test_size=0.3, random_state=0)
print('X_train')
print(x_train)
print()
print('X_test')
print(x_test)
print()
print('Y_train')
print(y_train)
print()
print('Y_test')
print(y_test)
