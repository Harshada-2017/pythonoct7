# create a list of 10 numbers and diplay the sum of last 4 elements 
# remove the items from the list located at 2nd and 5th position
# print the diff between max and min number between list
# append a new element in the list which is half of the item of 3rd position in the list 


numbers=[10,45,7,2,5,20,17,42,20]
print(sum(numbers))

numbers.pop(1)
numbers.pop(4)
print(numbers)
    

s=(sorted(numbers)) #ascending
print(s)
print(s[0])
print(s[-1])
print(s[0]-s[-1])

