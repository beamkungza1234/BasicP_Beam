dist = input("Distance Price Calulator\nEnter Distance: ")
dist = int(dist)

#debug
print(type(dist))

print("------------------------------------------------------")

if dist <= 4:
    print("Your distance is: ", dist, "\nNo price included")
elif 5 <= dist <= 50:
    print("Your distance is: ", dist, "\nPrice is 10 Bath")
elif 51 <= dist <= 100:
        print("Your distance is: ", dist, "\nPrice is 15 Bath")
elif 101 <= dist <= 300:
    print("Your distance is: ", dist, "\nPrice is 25 Bath")
elif 301 <= dist <= 500:
    print("Your distance is: ", dist, "\nPrice is 35 Bath")
elif dist > 500:
    print("Your distance is: ", dist, "\nPrice is 45 Bath")
else:
    print("Unknow distance. Please try again")
        
     