my_list=[]
print(my_list)

# with items
fruits=["apple","cherry","banana"]
print(fruits)
print(sorted(fruits))

# starts from zero to -1

numbers=[10,20,30,52,20,17]
print(numbers[0])
print(numbers[-2])

#append 
colors=["red","blue"]
colors.append("green")
print("after adding",colors)

colors.insert(1,"yellow")
print("After insertion at second position",colors)

colors.remove("yellow")
print(colors)

#lenght
print(len(numbers))
print(sum(numbers))
print(sorted(numbers)) #ascending
print(sorted(numbers,reverse=True)) #descending