# LOOPS 


#  1 . Print all numbers from 1 to 100 using a for loop 

for i in range(1,101): 
  print(i) 
#   or 

n=10
for i in range(1,n+1):
  print(i)


# 2.   Write a program to print the sum of the first n natural
# numbers. (n*n+1/ 2) 

sum=0
for i in range(1,101):
   sum+=i 
   print(i) 
print(sum) 

# or 
n=10 
sum=0
for i in range(1,n+1):
  sum+=i
  print(i) 
  print(sum) 
  # or shortcut 
# print((n*(n+1))/2)   

# 3.  Print all even numbers between 1 and 50 using a while
# loop  

# num=1
# while num<=50:
#   if(num%2==0): 
#     print(num)
#     num+=1 





# 5 .  Reverse a number using a while loop.
#   Also can we get the sum of all the digits  

num=54327 
rev_num=0  
sum=0 
count=0

while num>0:
  rem=num%10 
  rev_num=rev_num*10+rem 
  num=num//10 
  sum+=rem 
  count+=1 

print(rev_num)
print(sum) 
print(count) 

# 7. Write a program that keeps asking the user to enter numbers
# until they enter a negative number. Use a while loop.

while True:
  num1=int(input("enter a non negative number")) 
  if num1<0:
    break; 
# or 

# num1=0
# while num1>=0:
#   num1=input("enter a non negative number ")  


#  6 . Write a program to count the number of digits in a given
# number using a while loop .  

# num=1
# count=0
# while num<=10:
#   #  print(num)
#    count+=1 
# print(count)      



# 4 M : Print all numbers from 1 to 100 that are divisible by 3 and 5
# using a for loop.

for i in range(1,101):
  if(i%3==0 and i%5==0):
    print(i)  




#  3 M : Write a program to calculate the factorial of a number using
# a while loop 

num=int(input("enter a number to calculate the factorial"))
fact=1
while(num>0):
  fact*=num 
  num-=1
  print("the factorial is :",fact)  