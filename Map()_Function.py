                        ## Introduction to map() function :-

## --> map() is a functional programming tool and an example of higher order function i.e a
##              function that accepts another function as a paramater .

## --> map() is used to apply a given function to all the items of an iterable and return a map object[an iterator].

## --> It does not modify original data , just performs element-wise transformation.

                        ## Syntax of map()
                        ## map(function, iterable)

## map returns the result in the form of object so convert it into a list , because it uses a lazy loading technique,
##          which is still not initialized.

                        ## why map() is important in Data Science ???
## In data science we frequently -
## 1. Transform data sets
## 2. apply the same function to all the values.
## 3. performa feature scaling & encoding

## So map() helps us to write

## clean & efficient code .
## avoid loops
## improves readability & performance



## Example to understand map()

def square(x):
    return x**2

print(square(4))
print(square(5))

## suppose what if I have a list of numbers in that case we have two options :

## 1. directly use map() function
## 2. or pass a list to function, cerate an empty list iterate using for loop and append each element after operation .


## IT takes time to go with 2nd one
nums = [1,2,3,4,5,6,7,8]
print(list((map(square, nums))))


## Examples of map() function

## Example-1 : Find the square of each element in a list
nums = [1,2,3,4,5,6,7]
print(list(map(lambda x : x**2, nums)))

## Example-2 : Convert Temperature From Celsius to Fahrenheit
celsius = [0,10,20,30]
fahrenheit = list(map(lambda c : c*9/5+32, celsius))
print(fahrenheit)

## Example-3 : Convert list of strings to uppercase - using built-in function with map
words = ['data','science', 'sql']
upper = list(map(str.upper,words))
print(upper)

## Example-4 : Add two list element wise
list1 = [1,2,3]
list2 = [4,5,6]

added_list = list(map(lambda x,y : x+y, list1,list2))
print(added_list)

## Example-5 : map() to convert list of strings to integer

str_numbers = ['1','2','3','4','5']
int_numbers = list(map(int, str_numbers))
print(int_numbers)
print(str_numbers)

## Example-6 : Find the length of each string
words = ["AI","Tejas","SAM", "David","BMW"]
res = list(map(len,words))
print(res)

## Example-7 : Add 5 to each element in a list - example use case with evaluation expression
a = [10,20,30,40]
result = list(map(lambda x : x+5,a))
print(result)

## Example-8 : Check even or odd for each item in a list
nums = [1,2,3,4,5,6,7]

res = list(map(lambda x :'Even'if x%2==0 else 'odd', nums))
print(res)

## Example-9 : Extract last digit of each number
numbers = [123,456,789]
ext = list(map(lambda x: x%10,numbers))
print(ext)

def get_name(person):
    return person['name']

people = [{'name':"Rahul",'age':25},
          {'name':'kiran','age':24}
          ]

print(list(map(get_name, people)))



