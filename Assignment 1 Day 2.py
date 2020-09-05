# Assignment 1  Day 2

# 1. List and its default methods
# 2. Dictionary and its default methods
# 3. Set and its default methods
# 4. Tuple and its default methods 
# 5. String and its default methods


# 1. List and its default methods
 
print("\n\t\tList and Default \n")
l=["paju",14,"shruti",25,5.5,14,50,[4,2,7]]
l1=[89,65]
print("Original List = ",l)
l.append('Let\'s upgrade')
print("After Append() = ",l)
l.insert(4,"python")
print("After Insert() = ",l)
print("Length of list = ",len(l))
print("Count of 14 in list = ",l.count(14))
l.extend(l1)
print("After extending elements of l1 = ",l)


# 2. Dictionary and its default methods

print("\n\t\tDictionary and Default \n")
d1={"prajval":"python","pillu":"java","matin":"css"}
print("Original dictionary = ",d1,"\n")

d1["matin"]="database"
print("After changing record of matin = ",d1,"\n")

d1["shrutika"]="design"
print("After inserting new record = ",d1,"\n")

print("item of key prajval = ",d1.get("prajval"),"\n")

d1.update({"shrutika":"web design"})
print("update() to upadte item of shrutika = ",d1,"\n")    

print("Keys of dictionary d1 = ",d1.keys(),"\n")

print("Items of dictionary d1 = ",d1.items(),"\n")

d2=d1.copy()
print("d2 dictionary = ",d2,"\n")

print(d1.clear())


# Sets and its default methods

print("\n\t\tSets and its default methods\n")

s={"paju",5,"shruti",3125}
print("Original Set   =  ",s)

s.add(25)
print("After add()    =  ",s)    # add() used to add single element

s.update([5.6,25,2.1])
print("After update() = ",s)

print("Length od set  = ",len(s))    # length of set

s.remove(2.1)
print("After removing 2.1=",s)      #remove methods is used to remove elements from set

set1={1,2,3}
set2={"a","b","c"}
set3=set1.union(set2)
print("After union () = ",set3)

set3.clear()
print("After clearing set3 = ",set3)


# Tuple and its default methods

print("\n\t\tTuple and its default methods\n")

t=("paju",31,"shruti",25,31)
print(type(t))
print("Original tuple    =  ",t)

print("Length of tuple   =  ",len(t))

if "shruti" in t:           # to check element in tuple
    print("Yes, Shruti is in tuple!!!")
else:
    print("Shruti not found in tuple...")

# we cannot add items in tuple
# we cannot update items of tuple 

print("Counting 31 in tuple = ",t.count(31))

print("Possition of paju    = ",t.index("paju"),)


# String and its default methods

print("\n\t\tString and its default methods\n")

# capitalize()
str1="hello"
print("After capitalizing string = ",str1.capitalize())

# center()  -->  add spaces 
print("After center ()           = ",str1.center(50))

# endswith()
string="abc@gmail.com"
print("Is string endwith @gmail.com ? = ",string.endswith("@gmail.com"))

# find()
str1="Hey, I'm Prajval"
print("Finding Prajval in string = ",str1.find("Prajval"))

# lower()
print("String in lower case  = ",str1.lower())

# upper()
print("String in upper case  = ",str1.upper())

# replace()
print("After replacing Prajval with Paju = ",str1.replace("Prajval","Paju"))