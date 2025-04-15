list=[5,3,7]
print(list[0])
print(list[1])
print(list[2])

print(list[-1])

list[1] = 9
print(list)

#Example
grades = [9.0, 6.7, 8.5, 7.6, 9.8, 7.0]
print(grades)

n = len(grades)
print(n)

grades= grades+[6.2, 8.2, 5.9]
print(grades)

##Slicing lists
print(grades[2:5])

#Example2(Creating a copy of a list)
list2 = [9, 6, 8, 7, 9, 7]
list1 = list2
list2[1] = 10
print(list1)
print(list2)

#If we want to create a new unrelated copy of list2 with the name list1, then we need to  type list1 = list2[:]