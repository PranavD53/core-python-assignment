menu=["Pizza", "Burger", "Pasta", "Salad"]
def add_item(item):
    menu.append(item)
    print(f"Updated menu: {menu}")
def remove_item(item):
    if(item in menu):
        menu.remove(item)
        print(f"Updated menu: {menu}")
    else:
        print("Item is not available")
def check_item(item):
    if(item in menu):
        print(f"Availability: {item} is available")
    else:
        print(f"Availability: {item} is not available")

add_item("Tacos")
remove_item("Saad")
check_item("Pizza")


