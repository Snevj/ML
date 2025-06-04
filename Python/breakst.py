#break:- we skip the loop
# continue:- we skip the iteration

for i in range(12):
    if (i == 10):
        print("The value is skipped")
        break
    print(" 5 X", i, "=", 5*i)