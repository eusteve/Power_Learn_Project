my_list =[] #creation of an empty list 

my_list.append(10) #adds a a single element at a time 
my_list.append(20)
my_list.append(30)
my_list.append(40)

#print(my_list) checks through the list

my_list.insert(1,15) # the index then the value to the enter into the given index.

add_list = [50,60,70] #iterable
my_list.extend(add_list) 
my_list.pop()  

new_list_des = sorted(my_list,reverse=True)
final_list_order = sorted(new_list_des)#
print(final_list_order)

value = my_list[3]
#print(f"this {value} is of index 3") 
