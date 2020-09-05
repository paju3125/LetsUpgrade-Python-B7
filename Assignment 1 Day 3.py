# Assignment 1 Day 3

altitude=int(input("Enter current altitude = "))
if altitude<=1000:
    print("Safe to land !!!")
else:
    if(altitude<=5000):
        print("Bring down to 1000...")
    else:
        print("Turn Around...")