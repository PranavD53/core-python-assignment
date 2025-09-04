n=int(input("Enter total number of seats: "))
y=list(map(int,input("Enter booked seats: ").split()))
x=list(range(1,n+1))
booked=[w for w in x if w not in y]

def book_seat(s):
    if(s in booked):
        booked.remove(s)
        print(f"Seat number {s} is booked")
        print(f"Available seats: {booked}")
    else:
        print("Seat is not available")

def cancel_seat(s):
    if(s not in booked):
        booked.append(s)
        booked.sort()
        print("Cancelled seat succesfully")
        print(f"Available seats: {booked}")
    else:
        print("Not Cancellable")

book_seat(3)
cancel_seat(5)
