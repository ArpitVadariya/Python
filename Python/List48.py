#  This is List Program


print("\n to store data in list add values with comma saperated between two square bracket")
print("\n example :- ")
print("\n [1, 2, 3, 4, 5]")
print("\n\n")
list1 = ["physics", "chemistry", "maths"]
print(list1)


print("\n list1.append(""biology"")")
list1.append("biology")
print(list1)


print("\n count particular item in list we use list1.count('maths'))")
print(list1.count("maths"))


print("\n to find index of item use list1.index('maths')")
print(list1.index("maths"))
print(list1)


print("\n to remove item use list1.remove(physics)")
list1.remove("physics")
print(list1)


list1.reverse()
print("\n to reverse items use list1.reverse()")
print(list1)