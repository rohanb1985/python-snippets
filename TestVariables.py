name = "Ryan"
print ("Outside function at start of code - "+name)

def printName():
	global name
	print ("Inside printName function: "+name)
	name = "Maitrayee";
	
name = "rohan"
printName()

print ("Outside function at end of code - "+name)