from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np
import pandas as pd
df=pd.read_excel("c:\\users\\lenovo\\documents\\Data.xlsx","Sheet1")
df=pd.DataFrame(df)
print(df)
encoder=LabelEncoder()
x=df.apply(encoder.fit_transform)  #Applies fit-transform on every element
o_h_encoder=OneHotEncoder()
x=o_h_encoder.fit_transform(x).toarray()
print(x)

