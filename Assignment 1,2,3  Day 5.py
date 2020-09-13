# Batch 7 Day 5 Assignment 2 

# Prime numbers between 1 to 2500 using filter

def even(num):
    b=2
    f=0
    cnt=0
    for b in range(2,num):
        while b<num:
            if num%b==0:
                f=1
                
            else:
                if f==1:
                    break
                else:        
                    f=0
                    
            b=b+1
        if f==0:
            cnt+=1    
            return True

lst=list(range(2500))
lst_even=filter(even,lst)
print("\nPrime numbers between 1 to 2500 = ",list(lst_even))



# Batch 7 Day 5 Assignment 3

# make a lambda function for capitalizing whole sentence passed using arguments
# and map all the sentences in the list with the lambda function

lst=["hey , i am prajval","i am in ahmednagar"]
lst_capitalize=map(lambda string: string.title(),lst)
print(list(lst_capitalize))