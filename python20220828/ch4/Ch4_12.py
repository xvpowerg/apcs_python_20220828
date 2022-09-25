greet = "Hello"
print(id(greet),"->",greet)
greet += "!"
print(id(greet),"->",greet)


greet = "Hi,ed"
#greet[3] = "E"
print(id(greet),"->",greet)
greet = greet.replace("e","E")
print(id(greet),"->",greet)


str1 = "This is his dogs"
s = "is"

print(str1.find(s))
print(str1.rfind(s))
print(str1.find(s,5))
print(str1.find(s,10))

print(str1.find(s,5,12))
print(str1.rfind(s,5,12))
print(str1.rfind(s,10))
