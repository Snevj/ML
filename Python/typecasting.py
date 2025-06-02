# typecasting is changing the variable type
a= "1"
b= "2"
print(int(a)+int(b))
string = "3"
number = 4
sum = int(string) + number #this is an example of explicit typecasting

print("The sum of both the number is", sum)
 
#example of implicit typeCasting is below; and it is the automatically when the python,
#changes the datatyope accordig to the order to prevent the data loss
c = 5.6 #float
d = 4 #integer
print(c + d) #float