product_num = eval(input("Enter Number of products: "))
my_dict ={}
for x in range(product_num):
    productName = input("Enter Product Name: ")
    productPrice = int(input("Enter Product Price"))
    my_dict[productName] = productPrice

while True:
    productName = input("Enter Product name to get Price")
    if productName in my_dict:
        print("The price for your product is ", my_dict[productName])

    else:
        print("This product is not found in dictionary")

print(my_dict)
