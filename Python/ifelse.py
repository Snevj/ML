#conditional operators <, >, <=, >=, ==, !=
time = int(input("Enter the time Sir"))

#you have to enter the time wrt the 24 hrs system

if(12>time>0):
    print("Good Moring Sir")
elif(time == 12):
    print("Good Noon Sir")
elif(12>time>17):
    print("Good Afternoon Sir!")
elif(24>time>17):
        print("Good Night Sir!")
else:
     print("Please enter the time according to 24 hrs format")