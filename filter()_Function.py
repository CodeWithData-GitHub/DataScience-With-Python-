## Example to understand filter function -
def even(num):
    if num%2==0:
        return True
    else :
        return False

print(even(10))
print(even(5))
## The above function works prefectly fine but just for 1 particular element but what if I have
## 10 element, 20 , 30 etc . In that case well go with filter depending on the use case

nums = [1,2,3,4,5,6,7,8,9,10]
print(list(filter(even,nums)))

## Now lambda function with filter()
nums = [1,2,3,4,5,6,7,8,9,10]
greater_than_five = list(filter(lambda x : x>5, nums))
print(greater_than_five)

## filter function with lambda and multiple conditions
nums = [1,2,3,4,5,6,7,8,9,10]
result = list(filter(lambda x : x>5 and x%2==0, nums))
print(result)

## Now let us appy filter() function on dictionary
people = [{'name':"Rahul",'age':25},
          {'name':'kiran','age':32},
          {'name':'john', 'age': 21},
          {'name':'cathrine','age':35}
          ]

def age_greater_than_25(person):
    return person['age']>25

print(list(filter(age_greater_than_25,people)))