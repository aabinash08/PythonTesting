lists = [1,2,3,4,5,6,'Abinash',7,8,9,-1]
print(lists)

#Slicing it's need to print the set of portion in a Given List
lists = [1,2,3,4,5,6,'Abinash',7,8,9,-1]
print(lists[2:9])
print(lists[2:-2])
print(lists[:-3])
print(lists[3:])
print(lists[:])

#Add the element to the end of a lit by using append() method
a = [1,2,3,4,5,6,'Abinash',7,8,9,-1]
a.append("nova")
print(a)

#Add the element to the specific Index by using insert() method
a=[1,2,3,4,5,6,'Abinash',7,8,9,-1]
a.insert(2,"Monknight")
print(a)

#Remove the Element in a List by using remove() method
a=[1,2,3,4,5,6,'Abinash',7,8,9,-1]
a.remove("Abinash")
print(a)

#Delte statement used to delete the multiple elements or the entire statement
a=[1,2,3,4,5,6,'Abinash',7,8,9,-1]
del a [1]
print(a)


