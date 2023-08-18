import pandas as pd
from Product import Product
from StackClass import Stack

# Assuming you have already read the data into the DataFrame 'df'
df = pd.read_excel('Reading.xlsx', sheet_name='products')


print("%15s%20s%10s" %("Product Name", "Category", "Price"))
print("-"*50)

#lets save product objects into a list:
plst = []
productStack = Stack()
for index, row in df.iterrows():
    name = row['pName']
    category = row['Category']
    price = row['Price']
    
    currentProduct = Product(name, category, price)
    productStack.push(currentProduct)
    plst.append(currentProduct)
    currentProduct.discount(15)
    
    # Do whatever you want with the variables
    # print(f"product Name: {name}, type: {category}, cost: {price}")
   # print(currentProduct.descripe())
#    print("%15s%20s%10.2f" %(currentProduct.getName(), currentProduct.getCategory(), currentProduct.getPrice()))


for p in plst:
    print("%15s%20s%10.2f" %(p.getName(), p.getCategory(), p.getPrice()))

print("num of products:", productStack.size())
print("top product: ", productStack.peek().getName()) #check without getName what happens
"""
#read into dictonary
products_list = []
for index, row in df.iterrows():
    product_dict = {
        
        'ProductName': row['pName'],
        'Category': row['Category'],
        'Price': row['Price']
    }
    products_list.append(product_dict)

# Print the list of product dictionaries
print(products_list)
"""



