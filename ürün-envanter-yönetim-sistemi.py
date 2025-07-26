products = {}

def add_product():
    product_name = input("Please enter the name of the product you want to add: ")
    product_price = input("Please enter the price of the product: ")
    product_stock = int(input("Please enter the stock quantity of the product: "))
    product_category = input("Please enter the category of the product: ")

    products[product_name] = {
        "price": product_price,
        "stock": product_stock,
        "category": product_category
    }

    print(f"The product '{product_name}' has been added.")

def update_product():
    while True:
        product_name = input("Please enter the name of the product you want to update: ")
        if product_name not in products:
            print("Product not found.")
        else:
            break

    print("1. Update product price")
    print("2. Update product stock")

    choice = input("Please select an option (1-2): ")

    if choice == "1":
        new_price = input("Please enter the new price of the product: ")
        products[product_name]["price"] = new_price
        print(f"The price of '{product_name}' has been updated to {new_price} TL.")
    elif choice == "2":
        new_stock = int(input("Please enter the new stock quantity of the product: "))
        products[product_name]["stock"] = new_stock
        print(f"The stock quantity of '{product_name}' has been updated to {new_stock}.")
    else:
        print("Invalid selection.")

def delete_product():
    product_name = input("Please enter the name of the product you want to delete: ")
    if product_name in products:
        del products[product_name]
        print(f"The product '{product_name}' has been deleted.")
    else:
        print("Product not found.")

def list_products():
    if not products:
        print("No products found.")
    else:
        for product_name, details in products.items():
            print(f"Product: {product_name}")
            print(f"Price: {details['price']}")
            print(f"Stock: {details['stock']}")
            print(f"Category: {details['category']}")
            print("-----------------------")

while True:
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. List Products")
    print("5. Exit")

    choice = input("Please select an option (1-5): ")

    if choice == "1":
        add_product()
    elif choice == "2":
        update_product()
    elif choice == "3":
        delete_product()
    elif choice == "4":
        list_products()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid selection.") 
