#anything inside "", '' is known as string
#for writing a multiline string use """ """"
name = "!!!!!Sneh!!!!!"
print(name[0])
print(name[1])
#print(name[5]) it throws an error
print("Hello!!", name, "!!")
#In python the string is like an array of characters only
names= "Sneh, Shubham, Bkuye"
print(names[0:4])
fruit = "Mango"
print(fruit[0:3])
print(fruit[0:-3])#this -3 is representing 'len(fruit)-3' :this is called negative slicing
print(fruit.upper())
print(name.rstrip("!")) #it strips/removes the trailing characters only
print(name.replace("Sneh", "john")) #