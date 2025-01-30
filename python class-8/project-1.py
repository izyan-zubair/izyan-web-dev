fruits = ("apple" , "banana" , "cherry" ,"Orange" , "strawberry")
print("fruits trple:")
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])
print("first two fruits:", fruits[0:2])
for x in fruits:
    print(x)
print("apples count:", fruits.count("apple"))

numbers = (1, 2, 3, 4, 5 ,1 ,2 ,3 ,4 ,5)
fruitsSet = ("apple" , "banana" , "strawberry")
print("Fruits in the set:", fruitsSet)
print("number set:", numbers)

numbers.add(6)
fruitsSet.add("pineapple")
print("fruits after adding:", fruitsSet)
print("after adding 6:", numbers)
numbers.remove(3)
fruitsSet.remove("banana")
print("fruits after removing:", fruitsSet)
print("after removing 3:", numbers)

set1 = {1, 2, 3}
set1 = {3, 4, 5}

print("Union of set1 and set2:", set1.union(set2))
print("Intersection of set1 and set2:", set1.intersection(set2))
print("Difference of set1 and set2:", set1.difference(set2))