mytuple = ("apple", "banana", "cherry")

# print tuple
print(mytuple)

#  allow duplicates

DuplicateTuple = ("apple", "banana", "cherry", "apple", "cherry")
print(DuplicateTuple)

# length

print(len(DuplicateTuple))


# Create Tuple With One Item

thisTuple = ("apple",)
print(type(thisTuple))  # this is a tuple

thisNotTuple = ("apple")
print(type(thisNotTuple))# this is a string 

# tuple constructor

thisTuple1 = tuple(("apple", "banana", "cherry"))
print(type(thisTuple1))


# access tuple items
thisTupleAccess = ("apple", "banana", "cherry")
print(thisTupleAccess[1])

# negative indexing
thisTupleNegative = ("apple", "banana", "cherry")
print(thisTupleNegative[-1])

# range indexes
thisTupleRangeIndexes = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thisTupleRangeIndexes[2:5])