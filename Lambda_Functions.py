## Introduction to Lambda Functions in python :-

## --> A lambda function in python is an anonymous function [i.e a function without a name]
##              defined using lambda keyword.
## --> It can have 'n' number of arguments but works with only 1 expression.
## --> It is used for simple & short operation or as an argument to higher order function.

## Syntax of Lambda Function :

## lambda arguments : expression

## Example to understand lambda function :

def addition(a,b):
    return a+b

addition(2,3)

## Now the same function can be written using lambda function
add = lambda a,b : a+b

print(type(add))
print(add(5,6))
print(add(4,6))

## Another example
def even(num):
    if num%2==0:
        return True
    else :
        return False

print(even(12))
## Now the above function can be converted to lambda function as given below

res = lambda num : num%2==0
print(res(24))

## Example with multiple parametres

def addition(x,y,z):
    return x+y+z

print(addition(12,13,14))

addition = lambda x,y,z:x+y+z
print(addition(5,5,5))

## Examples of lambda function :
## Example-1 : Addition of two numbers
add = lambda a,b : a+b
print(add(2,4))
print(add(4,5))

## Example-2 : square of a number
sqr = lambda n : n*n
print(sqr(5))
print(sqr(6))

## Example-3 : Check if a number is even
even = lambda num : num % 2 ==0
print(even(25))
print(even(10))

## Example-4 : finding themaximum of two numbers
max_of_two = lambda a,b : a if a>b else b
print(max_of_two(2,3))
print(max_of_two(5,3))

## Example-5 : Multiply 3 numbers
mul = lambda a,b,c : a*b*c
print(mul(1,2,3))
print(mul(2,4,6))

## Example-6 : Convert celsius to fahrenheit
fah = lambda c : (c*9/5)+32
print(fah(32))

## Example-7 : Find the length  of a string
length = lambda s : len(s)
print(len("python"))
print(len("David"))

## Example-8 : Check if a number of postitive , negative or zero
check = lambda n : "positive" if n>0 else "negative" if n <0 else "zero"
print(check(5))
print(check(-2))

## Example-9 : Add 10 to a given expression
add_ten = lambda x : x+10-2+5
print(add_ten(10))

## Example-10 : Extract the last digit of a number
last_digit = lambda x : x%10
print(last_digit(2250))

## Example-11 : Check if a number is divisible by 5 or not
div5 = lambda x : x%5==0
print(div5(45))
print(div5(12))


## The power of lambda function with map()- Lambda can be used as an argument to higher order function

## map-applies a function to every element or item present in an iterable
nums = [1,2,3,4,5,6]
def square(num):
    return num**2
print(square(3))

res = list(map(lambda x : x**2, nums ))
print(res)





def addition(a,b):
    return a+b
print(addition(2,3))


res=lambda a,b : a+b
print(res(5,3))

def even(num):
    if num%2==0:
        return True
    else :
        return False
print(even(24))
print(even(9))

def sum_of_three(x,y,z):
    return x+y+z
print(sum_of_three(1,2,3))

result = lambda a,b,c : a+b+c
print(result(5,10,15))