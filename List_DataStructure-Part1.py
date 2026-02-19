                                ## Introduction To List :

## --> A list in python is an ordered, mutable collection of elements that can store
##          data of heterogeneous type but allows duplicate values.

## --> list is ordered which means elements inside it follows insertion order

## --> Allows duplicate values

## --> List is mutable i.e elements can be modified after creation.

## It supports indexing & slicing operation through which elements can be accessed using
##           index values.

                                ## Features of list

## 1. Ordered : Elements inside a list follows insertion order
## 2. Mutable : Elements can be modified after creation.
## 3. Indexing & slicing : List supports indexing & slicing operations and elements are acccessed using index values
## 4. Duplicate values : List allows duplicate values meaning a same element can appear multiple times .
## 5. Heterogeneous : Stores data of different data types .
## 6. Iterable : It can be traversed using loops

## 1- Creating an empty list
empty_list = []
print(empty_list)
print(type(empty_list))

## 2- Creating list with integer values
my_list = [10,20,30,40,50]
print(my_list)

## 3- Creating list containing strings
my_list1 = ["Rock","Table","Pencil","Pen"]
print(my_list1)

## 4- Creating a mixed list
mixed_list = [10,20," Python",3.14,True]
print(mixed_list)

## Indexing - It allows us to access indvidual elements using their index positions
## Types of indexing :
## 1. Positive indexing : starts from 0 [traverse a list from left to right]
## 2. Negative Indexing : Starts from -1[traverse a list from right to left]

fruits = ['apple','mango','banana','guava','pineapple']
print(fruits)

print(fruits[0])
print(fruits[1])
print(fruits[4])
print(fruits[-1])

## here the last element can be accessed in two ways, it can be either postive or negative indexing
print(fruits[-2])
print(fruits[-4])


## Slicing operations : It extracts a portion of a list uing start, stop & step values
## syntax - list[start : stop: step:]

nums = [10,20,30,40,50,60]
print(nums)
print(nums[1:])
print(nums[0:3])
print(nums[0:5])
print(nums[4:])

## special case : To reverse a given list using Scope resolution operator i.e ::
print(nums[::-1])

                                    ## Modifying List elements
print(fruits)
## Now i want to replace the mango item to kiwi in the 1st index
fruits[1]="Kiwi"
print(fruits)
fruits[1:]="kiwi"
print(fruits)
## With the 2nd example there is a problem it is not replacing the item by word but with character by character.


nums = [5,8,15,20]
nums[1]=10
print(nums)

                                    ## List operations
## 1. Concatenation - It combines two or more list into a single list
list1 = [1,2,3]
list2 = [4,5,6]
result = list1+list2
print(result)

## 2. Repetition : It repeats the elements of a list multiple times
nums = [10,20]
print(nums*3)

## 3. Membership [in/not in] : It checks whether an elements exists in a list or not
num = [5,10,15,20]
print(5 in num)
print(20 not in num)
print(25 not in num)

## 4 . Length : It returns the number of elements present in a list
nums = [10,20,30,40,50]
print(len(nums))

## 5 . Iterations : Traversing each element one by one
nums = [1,2,3,4,5]
for value in nums:
    print(value)

## 6. Comparison operation : Compares two list element by element .
a = [1,2,3]
b = [1,2,4]
print(a==b)
print(a<b)

## Iterating over list ;
numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    print(num)

## next if I want to iterate this list with index as well - how to do that ?? we have one
##      in-built function called enumerate() function which prints elements with their corresponding index
for index,num in enumerate(numbers):
    print(index,num)
