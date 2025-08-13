'''Lists:
Collection of items
Different data types allowed
Mutuable
Ordered
Nesting allowed
'''

'''
items=["english", "hindi"]
print(items)
item=[1.0,3,"string"]
print(item)
#indexing
#slicing
print(item[0:2])  


item.insert(1,"string0") #insert method
print(item)
item.append(6) #append method

print(item)
item[2]=5 #reassigning
print(item)

item.pop() #pop method
print(item)

item.pop(0) #pop with index
print(item)

item.remove(5) #remove
print(item)

'''
numbers=[33,11,66,99,44]
print(sorted(numbers))  #sorted method

number=[66,33,22,1,6,87,23,97,999]
print(number[1:8:3])
print(number[:5:2])
 #sort method
number.sort()
print(number)

print(number[:8:3])


number.reverse() #reverse
print(number)

print(sum(number)) # sum method
