def check_Prime(num):
    if num > 1:
   # check for factors
        for i in range(2,num):
            if num % i == 0:
                print("Not prime number")
             
                break
        else:
            print("Prime number")
       
# if input number is less than
# or equal to 1, it is not prime
    else:
        print("Not prime number")

