
# <!-- write a program to check if a given number is positive, negative  or zero 
#   -->

# a=int(input("enter a number"))
# if a>0:
#   print("positive number")
# elif(a<0):
#     print("negative number")
# else:
#     print("zero number") 

    # 2. determine if a number is even or odd 
# num=2
# if(num%2==0):
#     print("even number")
# else:
#     print("odd number")   

#  print("even") if num%2=0 else print("odd") = using terinary operator 

#  3. check if a person is eligible to vote ( age>=18) 

# num=int(input("enter age"))
# if(num>=18):
#     print("eligible to vote") 
# else:
#     print("not eligible to vote")  


#  4. write a program to find the greatest of two numbers  

# num1=int(input("enter first number"))
# num2=int(input("enter second number"))
# if(num1>num2):
#    print("num1 is greater") 
# elif(num2>num1):
#    print("num2 is greater")
# else:
#    print("both are equal") 




# 5 print "pass" if a student scores morethan 40 marks , otherwise fail 

# num=int(input("enter marks"))
# if(num>40):
#     print("pass")
# else:
#     print("fail") 

# 6. write a program to display the day of the week based on a number input(a for monday , 2 for tuesday etc)
# week=int(input("enter a number in a day")) 
# if(week==1):
#     print("monday")
# elif(week==2):
#  print("tuesday")
# elif(week==3):
#    print("wednesday")
# elif(week==4):
#    print("thursday")
# elif(week==5):
#    print("friday")
# elif(week==6):
#    print("saturday")
# else:
#    print("sunday") 


# 7. implement a simple calculator to perform addition , subtraction, multiplication and division .  

# num1=input("enter first number")
# num2=input("enter second number")
# optr=input("enter a operator" ).lower()
# if(optr=='add' or optr=='+'):
#     print(num1+num2) 
# elif(optr=='sub' or optr=='-'):
#     print(num1-num2)
# elif(optr=='mul' or optr=='*'):
#     print(num1*num2)   
# elif(optr=='div' or optr=='/'):
#     if(num2==0):
#         print("division is not possible")
#     else:
#         print(num1/num2)
# else:
#     print("invalid operator")        


# 8  write a program to display name of the month based on month number 

# month=input("enter month number (1-12)")
# names=["january","february", "march","april","may","june","july","august","september","october","november","december"]

# if 1<= month <=12:
#     print(names[month-1]) 
# else:
#     print("enter valid month number")




# 9// write a program to find the greatest of three numbers 

num1=10
num2=20
num3=40
if(num1>num2 and num1>num3):
 print("num1 is greatest number")
elif(num2>num1 and num2>num3):
    print("num2 is greatest number")
elif(num3>num1 and num3>num2):  
    print("num 3 is greatest number")  
else:
    print("all numbers are equal") 

# 10 // Check if a year is a leap year.
year=int(input("enter a year")) 
if(year%400==0): 
    print("it is a leap year") 
elif(year%100==0):
    print("it is not a leap year") 
elif(year%4==0):
    print("it is a leap year")
else:
    print("it is not a leap year") 

# 11  calculate the grade of a student based on the marks they score

#    90-100: Grade A
#    80-89: Grade B
#    70-79: Grade C
#    <70: Fail.

marks=int(input("enter your marks here"))  
if(marks<70):
    print("you are fail")
elif(marks<=79):
    print("you are grade C")
elif(marks<=89):
    print("you are grade B")    
else:
    print("you are grade A")  


# 12    Write a program to check if three sides length form a valid
# triangle.  

side1=int(input("enter length of the first side"))
side2=int(input("enter length of the second side"))  
side3=int(input("enter length of the third side"))


if(side1+side2>side3 and side2+side3>side1 and side1+side3>side2):
    print("three sides length form a valid triangle") 
else:
    print("do not form a valid triangle ")     