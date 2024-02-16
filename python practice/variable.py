#variable = value
#a=10
#print(a)


#many values  many variables assign
#a,b,c=1,2,3
#'same we can use example like'
# x, y , z= "teja", "raju", "mahi"
#print(b)
#print(a)
#print(c)

#x=21,12,13
#print(x)

#x=y=z=40.5
#print(x,y,z)

#it shows memory location id
#abc123=50
#print(id(abc123))

#Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)