print("list in python")
fruits = [ "apple" ,"banana" , "cherry"]
print("Original list :", fruits)

fruits.append("Orange")
print("After appending Orange :", fruits)

fruits.remove("banana")
print("After removing banana :", fruits)

print("first element of list :", fruits[0])

print("Iterating through the list")
for fruits in fruits:
    print(fruits)

print("/nDictionary in python")

students= {"name": "John", "age": 20, "city": "New York"}
print("Original dictionary :", students)

print("name of student", students["name"])

students["school"] = "ABC high school"

students["age"] = 21
print("After updating 'age' :", students)

del students["grade"]
print("After deleting 'grade' :", students)

print("Iterating through the dictionary")
for key, value in students.items():
    print(key, ":", value)

lst = ["Apple" ,"mango" , "banana" , "cherry" , "grapes"]

print("length of list :", len(lst))
print("first element of list :", lst[0])
print("last element of list :", lst[-1])

lst.append("orange")
print("Updated list :", lst)

lst.remove("mango")
print("Updated list :", lst)

lst.sort()
print("Sorted list :", lst)

lst.pop(1)
print("Updated list :", lst)

lst.reverse()
print("Reversed list :", lst)

print("Multidimensional list", lst*2)

lst = lst[:4]
print("Updated list :", lst)

lst.clear()
print("Updated list :", lst)

obj = {'name': 'John', 'age': 30, 'city': 'New York'}

print(obj['name'])
print(obj.get['age'])

obj['age'] = 27
print(obj)

obj['address'] = 'Downtown'
print(obj)

obj.pop('age')
print(obj)

obj.clear()
print(obj)