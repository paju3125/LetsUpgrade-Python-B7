# Day 9 Assingment 2

# Make a small generator program for returning armstrong numbers in between 1-1000
# in a generator object

def getArmstrongnumber(lst):
    for item in lst:
        sum = 0  
        temp = item  
  
        while temp > 0:  
            digit = temp % 10  
            sum += digit ** 3  
            temp //= 10  
  
        if item == sum:  
            yield item
        else:  
            pass

lst=list(range(1,1000))
print(list(getArmstrongnumber(lst)))