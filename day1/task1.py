
# task 1: how to declare different types of datatypes 

# DATATYPES IN PYTHON :
#  1. BUILT IN DATATYPES
#  2. CUSTOM DATATYPES
# 1. BUILT IN DATATYPES: 
# . numeric types: int, float, complex, boolean
# . sequence types: list , tuple, string, range
# .mapping type: dictionary(key and value pairs)
# . set type: set
# . none 

# int example : 
integer_example=10 
print(integer_example) 
print(type(integer_example)) 

# float example 
float_example=3.21
print(float_example)
print(type(float_example)) 

# complex example 
complex_example=2+3j
print(complex_example)
print(type(complex_example)) 

# boolean example 
bool_example=True
print(bool_example)
print(type(bool_example)) 

# list example  : mutable and collection of items in ordered
list=[1,2,3,4]
print(list)  
list.insert(2,4)
print(list)
print(type(list))  

# string example : sequence of characters . immutable 
str="hello welcome to world"
print(str)
print(type(str)) 

# tuple example  : immutable AND collection of items 
tuple=(2,1,3,4)
print(tuple)
print(type(tuple)) 

# range example : sequence of numbers it is used in loops

range_example=range(10)  
print(range_example)
print(type(range_example)) 


# dictionary example 
person={ "name":"swetha", "age":21,"city":"hyd"}
print(person)
print(type(person)) 

# set example  : it is unorderd collection of  unique items 
example={3,2,1,4,5,2}
print(example)
print(type(example)) 

# None type : represents the absence of value 
example=None
print(example)
print(type(example))


# TASK 2:   operators  in python 
# 1. ARITHMETIC OPERATORS :
# . addition(+) , subtraction(-) , multiplication (*), division(/), modulus(%), floor division (//)(quotient) ,exponentiation (**) 

a=10
b=5
print(a+b) 
print(a - b)  
print(a * b)  
print(a / b)  
print(a // b) 
print(a % b)  
print(a ** b)  

# 2. COMPARISON OPERATORS : used to compare two values. they return true or false based on the comparison.
# .equalto(==), not equal to(!=),greaterthan (>), lessthan (<), greaterthan or equal to (>=), lessthan or equal to(<=) 

a=9
b=3
print(a == b)  
print(a != b)  
print(a > b)   
print(a < b)   
print(a >= b)  
print(a <= b)  

# 3. LOGICAL OPERATORS : these are used to combine conditional statements 
# and , or ,not  

a=10
b=5
print(a > 5 and b < 10)   
print(a<5 or b<10)  
print(not(a > b))  

# 4. ASSIGNMENT OPERATORS :  these are used to assign values to variables 
# assigns a value (=), add and assign (+=),subtract and assign(-=),multiply and assign (*=),: Divide and assign(/=), Floor divide and assign(//=), Modulus and assign(%=), Exponentiate and assign(**=) 

a=10
a+=5
a-=15
a*=2
a/=2  

# 5. BITWISE OPERATOR  : these operators perform bit level operations on integers

#  (&) bitwise AND  
#  (|) bitwise OR 
#  (^) bitwise XOR 
#  (~) bitwise NOT
#  (<<) bitwise leftshift
# (>>) bitwise right shift 

a=5 

b=3
# 5=0101
# 3=0011
print(a & b) 
print(a ^ b) 
print(~a) 
print(a << 1)
print( a>> 1)  

#3.  CONDITIONAL STATEMENTS  *IF *ELSE *ELIF

# these are used to execute a certain block of code based on the condition is true or false .
# IF : it is used to test a condition .if the condition is true then execute block of code .

x=10
if(x>5):
    print("x is greater than 5 ") 

    # IF ELSE :  else block is used to execute the code when the condition is false .
    x=10
    if(x>12):
        print("x is greater than 4 ")
    else:
        print("x is lessthan 4") 

#    IF-ELIF-ELSE (ELIF): the elif statement is used to check multiple conditions . if the first condition is false then moves to next elif statement , and so on .if none of the conditions are false then execute else block statement .

# x=8
# if (x>10):
#     print("x is greater than 10") 
# elif(x==8):
#     print("x is equal to 8") 
# else:
#     print("x is lessthan 8") 

# NESTED IF : 
    # X=10
    # Y=20
    # if (X>5): 
    #     if(Y>15):
    #         print("X is greater than 5 and Y is greater than5")

# 4. loops : used to execute a block of code repeatedly as long as a specific condition is met.

# 1. FOR LOOP : it is used to iterate over a sequence and execute block of code for each item in the sequence .
    fruits=["apple","orange","banana"]
    for i in fruits:
        print(i)  
print(type(fruits)) 

# example with range 
for i in range(1,10):
    print(i) 
print(type(i)) 

# example with tuple 
fruits=("banana","cherry","apple")
for i in fruits:
    print(i) 

# 2.  WHILE LOOP : while loop runs as long as the condition is true. if the condition is false the loop stops.

# x=10
# while(x==10):
#     print("x is equals to 10 ")  
x=0
while(x<5):
    print(x)
    x+=1 

# 3. BREAK STATEMENT :  it is used to exit the loop early, regardless of the condition
    for i in range(10):
        if i==5:
            break 
        print(i)  

# 4. CONTINUE STATEMENT : it is used to skip the current iteration of the loop and  moves to the next one. this is useful when you want to skip the some part of the loop under certain conditions 
    for i in range(5):
       if i==3:
        continue 
       print(i)  


# task 6:  INBUILT FUNCTIONS :

# STRING FUNCTIONS :  these are used to manipulate and process strings .
    name="python" 
    print(len(name)) 

    word="hellO"
    print(word.upper())
    print(word.lower())  

#   split :split  a string into list 
    a="hello world"
    print(a.split()) 

# replace : replace old with new

    a="i love python"
    print(a.replace("python","js")) 

#  concatenation 
    a="hello"
    b="welcome" 
    print(a+" "+b)  

# LIST FUNCTIONS :  these functions are used to interact with the lists 
fruits=["apple","banana","orange"]
print(len(fruits)) 

# sorted order 
number=[1,3,2,4,1,6,7,29,8]
print(sorted(number)) 

# list iterable convert tuple or string into list 
# tup=(1,2,34)
# print(list(tup)) 

# APPEND : adds an item to the end of the list 
fruits=["apple ", "banana","cherry"]
fruits.append("orange") 
print(fruits) 

# EXTEND : adding multiple items in a list
fruits=["apple","banana"]
fruits.extend(["kiwi","cherry"])
print(fruits)
 
#  POP : REmoves last item in a list
fruits=["apple ", "banana","cherry"]
fruits.pop()
print(fruits)
       


# task 5 : FUNCTIONS IN PYTHON 
 
    # A function is a block of code which only runs when it is called. 
    # You can pass data, known as parameters, into a function. 
    # A function can return data as a result. 

    # Declaring a function
def greet(name):
        return f"Hello, {name}!"

    # Calling a function
result = greet("Alice")
print(result)  # Output: Hello, Alice!

    # Example of a function with a return statement
def add(a, b):
        return a + b

    # Calling the function
sum_result = add(10, 5)
print("Sum:", sum_result)  # Output: Sum: 15
    
