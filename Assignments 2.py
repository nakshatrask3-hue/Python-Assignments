#To create a set of fruits
set_1 = {"Apple","Banana","Cherry"}
print("Your elements in the set 1 are:",set_1)
set_2 = {10,20,30,"Cherry"}
print("Your elements in the set 2 are:",set_2)

#Taking the union of both the sets
union_sets = set_1| set_2                 #Union of the set
print("The union of the set is:",union_sets)

#To take the intersection of the elements
intersection_sets = set_1 & set_2             #Intersection of the set
print("The intersection of the sets is:",intersection_sets)

#To take the difference of the elements
difference_sets = set_1 - set_2               #Difference of the two sets
print("Your difference of the two sets is:",difference_sets)

#To add the elements in a set
set_1.add("Mango")                 #Adding mango fruit
print("The fruit added is:",set_1)

#To remove particular element of the set
set_2.remove("Cherry")
print(set_2)                         #Removing "Cherry" from set 2

set_2.discard(30)
print(set_2)                       #Discarding the element from set 2
