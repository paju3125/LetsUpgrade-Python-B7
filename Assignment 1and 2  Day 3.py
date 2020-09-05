# Assignment 1 Day 3

altitude=int(input("Enter current altitude = "))
if altitude<=1000:
    print("Safe to land !!!")
else:
    if(altitude<=5000):
        print("Bring down to 1000...")
    else:
        print("Turn Around...")



# Assignment 2 Day 3

# pritn all the prime numbers between 1-200 using for loop and range function

a=2
for n in range(2,201):
    for a in range(2,n):
        if n%a == 0:
            break
    else:
        print(n,end="  ")
        