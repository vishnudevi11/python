import pandas as pd


#
# data={
#     'Name':['Alice','Bob','Charlie'],
#     'Age':[20,30,40],
#     'City':['New York','salem','paris']
# }
#

# automatically it will convert

# df=pd.read_csv("data.csv")
# print(df['Age'])
# df['Age'].to_csv("output.csv",index=False)
# to convert csv file
# df.to_csv("output.csv",index=False)

#df=pd.DataFrame(data)
# print(df.dtypes)
# print(df['Name'])

# df=pd.read_csv('data.csv')  #reading csv file
# df['Total']=df['Price']*df['Quantity'] #calc
# grouped=df.groupby('Product')['Total'].sum().reset_index() #group by product
# sorted=grouped.sort_values('Total',ascending=False)
# print(sorted)


# how to read json file

# df=pd.read_json("file.json")
# print(df)


# joining dataframe
# customers=pd.DataFrame({
#     "CustomerID":[1,2,3],
#     "CustomerName":["Vishnu","Devi","Naga"],
# })
#
# orders=pd.DataFrame({
#     "OrderID":[1,2,3],
#     "CustomerID":[1,3,2],
#     "Product":["Shirt","Pant","Sheos"],
# })
# result=pd.merge(customers,orders,on="CustomerID",how="inner")
# print(result)

# using coditions
df=pd.DataFrame({'x':[1,2,3,4,5]})
result=df[df['x']>3]
print(result)