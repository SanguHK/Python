#Sets
''' Unique elements
Unordered
unidex
no duplicate elements
{,element1,element2... elementn
}
 '''
s={1,2,3,3,4,5,6} #unique only
print(s)

sets=set([1,3,"sangu","amar"]) #creating set with set function
print(sets)


# to create a empty set
s4=set()
print(s4)
print(type(sets)) # finnding  class


#sets operations5
s1={2,3,4,6}
s2={6,7,4,8}

print(s1.union(s2)) #union
print(s1 | s2)

print(s1 & s2) #intersection

print(s1-s2) #difference

#set methods
s1.add(10) #adding ekement
print(s1)

s1.pop() #removes random element
print(s1)

s1.remove(4) # remove method to remove particular element
print(s1)