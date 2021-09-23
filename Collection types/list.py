myList = ['a', "b", "abab"]
# list extend
'''
school = ["primary", "Secondary"]
hSchool = ("Prep", "Uni")
print('--#1. ', school)
print('--#2. ', hSchool)
school.extend(hSchool)
print('--#3. ', type(school)) 

'''

# Remove list items
''''

print(myList)
# myList.pop()
# del myList[0]
# del myList
myList.clear()
print(myList)

'''

# Loop through the list
'''

mylist = ['a', True, False]
# for i in mylist:
#     print(i, "\n world")

# for i in range(len(mylist)):
#     print(mylist[i])

# i = 0
# while i < len(mylist):
#     print(mylist[i])
#     i = i + 1

# [print(x) for x in mylist]


'''

'''
List Comprehension

newList = []
print('--#1. newlist = ', newList)
for x in myList:
    if "a" in x:
        newList.append(x)
print('--#2. newlist = ', newList)

newList = [x for x in range(10) if x % 2 == 0]
print(newList)

'''

'''
# Sort list

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=False)
print(thislist)


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
'''

# '''
# Copy list
# thislist = ["apple", "banana", "cherry"]
# mylist = list(thislist)
# print(mylist)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list2 + list1
# print(list3)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = []

for x in list2:
    list3.append(x)
for x in list1:
    list3.append(x)

print(list3)
# '''
