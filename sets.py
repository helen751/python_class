#creating a set in python
s1 = {'a','b','a','c'}
s2 = {1, 2, 3, 4, 5}

name = ["Helen","john",45]
#updating th value in the first element of the list
name[0] = "faith"
name_set = set(name)
print(set(name)) 
print(s1)

#type casting
a = 12
print(a)
print(float(a))

# adding to a set
name_set.add("loreth")
list2 = ["loreth", "favour", "grace"]
name_set.update(list2)

#set functions for update and union
lang1 = {"C++","C#","Java","PHP","Dart"}
lang2 = {"PHP","Rust","Go","Flutter"}
lang1.update(lang2)
lang3 = lang1.union(lang2)

print(lang1)
print(lang3)
print(name_set)

