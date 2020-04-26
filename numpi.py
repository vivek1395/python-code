import pandas as pd

dict1={"name":['vivek','vishal','Nirod'],"marks":[22,18,13], "age":[28,24,29]}
print(dict1)
df1=pd.DataFrame(dict1)    # creating dataframe
print(df1)   # printing dict in dataframe structure
print("I am slice the datafram see below")
print(df1.head(1))
print(df1.tail(1))

dict={"name":['vivek','vishal','Nirod'],"marks":[22,18,13], "age":[28,24,29]}


dict2={"name":['surya','dipu','tosali'],"marks":[17,19,12], "age":[30,24,31]}
df2=pd.DataFrame(dict2)
print(df2)
df1=df1.join(df2)

print(df1)






