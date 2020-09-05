# Assignment 1 Day 4

# print the first armstrongnumber in the range 1042000 to 702648265 and break the loop as soon as 
# you encountered first armstrong number.

a=1042000
b=702648265
cnt=0
for num in range(a,b):
  length=len(str(num))
  temp=num
  sum=0
  while temp>0:
      digit=temp%10
      sum=sum+digit**length
      temp=temp//10
      if sum==num:
        print ("First armstrong number is ",num)
        cnt=1
  if cnt==1:
    break      
    