#Inventory can be defined statically as below or can be created on run time
# by calling create_inventory() function
""" inventory =[
    {'s_no': 1, 'item': 'Biscuits', 'Quantity': 4, 'price': 10}, 
    {'s_no': 2, 'item': 'Chips', 'Quantity': 3, 'price': 10}, 
    {'s_no': 3, 'item': 'Frooty', 'Quantity': 2, 'price': 5}, 
    {'s_no': 4, 'item': 'Aloo bhujia', 'Quantity': 2, 'price': 10}
    ]"""

inventory = []
s_no = 0

# Below function creates a dictionary item based on user input values 
# and appends it to inventory list

def create_inventory():
    global s_no
    n = int(input('No. of distinct items: '))
    while len(inventory)!=n:
        item_name = input('Name of the item: ')
        quantity = input('No. of items available: ')
        price = input('Price of one item: ')
        if item_name and quantity and price:
            item = {}
            item['s_no'] = s_no + 1
            item['item'] = item_name
            item['Quantity'] = int(quantity)
            item['price'] = int(price)
            s_no = item['s_no']
            inventory.append(item)
#            print(inventory)
        
        else:
            print('Item name, quantity or price can not be null...Try again!')
            break

# Purpose of below function is to provide an easy display interface.  

def display():
    print('\nHi! We have below items available at this moment...\n')
    print("S_no\tQuantity\tPrice\t\tItem")
    for item in inventory:
        if item['Quantity']>0:
            print(f"{item['s_no']}\t{item['Quantity']}\t\t{item['price']}\t\t{item['item']}")

# This function provides the main functionality of application.
# first it displays the menu.
# then asks for user selection of item and its price.
# once item extracted it will strat over again with updated menu.
# Press 0 to exit.

def extraction():
    while(True):
        display()
        selection = input('\nWhat would you like to have(0 to cancel)?')
        if int(selection)==0:
            break

        found = False
        for item in inventory:
            # check if item exists.
            if item['s_no'] == int(selection):
                found = True
                input_price = int(input('Insert the money: '))
                #check if price is correct.
                if item['price'] == input_price: 
                    #update inventory
                    item['Quantity']  = item['Quantity'] - 1
                    print(f"Good Choice, here is your {item['item']}. Have a nice day.")
                else:
                    print('Please insert the correct money..')
                    continue
        if found == False:
            print('\nInvalid Choice.. Try Again!!')
        

if __name__=='__main__':
    create_inventory()
    extraction()