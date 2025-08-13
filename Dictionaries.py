 #Dictionaries
'''
#Stores key value pairs
Syntax:
dict={key1:value1,
key2:value2,
...
keyn:valuen}

#access value using key
#Unordered 
#mutable
'''

ipl={
    "bng":"rcb",
    "mb":"mi",
    "klk":"kkr",
    "hyd":"srh",
    "chn":"csk",
    "pnb":"pbks"
}
print(ipl)
print(type(ipl)) #to find class


#accessing values
print(ipl["chn"]) #using key 

#To safe access
print(ipl.get("klk")) #get()


#Adding an key value to dictionary during runtime
ipl["rjs"]="rr"
print(ipl)

#To modify or update
ipl["pnb"]="kxip"
print(ipl)

#Removing an elements

x=ipl.pop("chn") #pop(key)
print(x)

del ipl["pnb"] #del  keyword
print(ipl)

#to get keys
print(ipl.keys()) #keys()

#To get values 
print(ipl.values()) #values()

#to get pair of key-value
print(ipl.items()) #items()


#Update dictionary with another
IPL={"ipL":"indian premier league"}
ipl.update(IPL)   #update()
print(ipl)




