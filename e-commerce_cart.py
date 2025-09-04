def calculateTotal(items):
    res=sum(items.values())
    if(res>0):
        if(len(items.values())>5):
            return res-(res*0.1)
        else:
            return res
    else:
        return "Cart is Empty"

cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
if(sum(cart_items.values())==0):
    print(calculateTotal(cart_items))
else:
    print("Total amount is ",calculateTotal(cart_items))