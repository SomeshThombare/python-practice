shipping_cart = {}

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Add Products | 2. Remove Products | 3. Display All Products | 4. Expensive Product| 5. Bill | 6. Exit")
        choice = input("Enter choice: ")

        if choice == 1:
            cust_id = input("Enter Cust ID: ")
            name = input("Enter Name: ")
            product_name = input("Enter Product Name: ")
            price = int(input("Enter Price: "))
            qty = int(input("Enter Qty: "))

            if cust_id not in shipping_cart:
                shipping_cart[cust_id] = {'name': name, 'Cart' :  []}
            item = {'product' : product_name , 'price': price, 'qty': qty}
            shipping_cart[cust_id]['cart'].append(item)
            print('Item added.')

        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass

        elif choice == 5:
            pass
        elif choice == 6:
            break
menu()