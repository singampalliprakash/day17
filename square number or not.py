num=int(input("enter the number:"))
if num>0:
    root=int(num**0.5)
    if (root*root)==num:
        print(f"the given {num} number is a square number")
    else:
        print("not a square number")
else:
    print("it is not a square number")
