menu = {
    "Coffee" : 2,
    "pasta": 3,
    "Pizza": 5,
    "Burger":6,
    "Chicken":10

}
print(
    """welcome to Zobayer's restaurant . please order Food!
    Coffee : 2$
    pasta :$3
    Pizza :$5
    Burger :$6
    Chicken : $10
    """
)
total_price = 0

ordered_items = []

while True:

    item = input("Enter the name of the item you want to order:")

    if item in menu:
        total_price += menu[item]
        ordered_items.append(item)
        print(f"your ordered {item} ,you total order is ${total_price}")
    else:
        print("Invalid item, please order something from the Menu")
    
    another_order = input("Do you want to add another item?(yes/no)").strip().lower()
    if another_order != "yes":
            break
            
print(f"\nyou orderd :{' ,'.join(ordered_items)}")
print(f"Total :${total_price}.Thanks you for ordering from zobayer's resturent!")