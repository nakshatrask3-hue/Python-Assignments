#To create a list and do opperations on it.
my_lst_1 = [10,20,30,"forty",50]
print("Your list is",my_lst_1)

#To acces list elements
print(my_lst_1[0])
print(my_lst_1[3])

#To add elements in a list using append and insert  
my_lst_1.insert(5,'60')     #Using insert 
my_lst_1.append(70)         #Using append 
print(my_lst_1)

#To remove the elements 
my_lst_1.remove('forty')
print(my_lst_1)            #Using remove
my_lst_1.pop(-1)
print(my_lst_1)            #Using pop

#To modify the elements of the list
my_lst_1[1] = 'Twenty'
print(my_lst_1)

#To clear the elements of the list
my_lst_1.clear()
print(my_lst_1)

#To sort the elements of the list
my_lst_1.sort()
print(my_lst_1)