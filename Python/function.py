# def isGreater(a, b):
#     if (a>b):
#         print(" First number is greater")
#     else:
#         print("Second is greater")

# a = 23
# b = 22
# isGreater(a, b)

# def isLesser(a, b):
#     pass
def average(*numbers):
    sum = 0
    # print(type(numbers)) #it tells the class of numbers
    for i in numbers:
        sum = sum + i
    # return 7 #always when we type the return, the function always accepts the return which is written first
    return sum / len(numbers)

c = average(1, 3, 4 ,5,6)
print(c)