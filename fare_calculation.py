def disp_calc_fare(trips):
    sum=0
    for i in range(len(trips)):
        print(f"Trip {i+1}:${50+(10*trips[i])}")
        sum+=50+(10*trips[i])
    print(f"Total Fare:${sum}")

n=int(input("Enter number of trips: "))
trips=[]
for i in range(n):
    x=int(input(f"Enter the number of kms for Trip {i+1}:"))
    trips.append(x)
disp_calc_fare(trips)