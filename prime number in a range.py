def isPrime(num: int) -> bool:
    num=input("enter the number:")
    if num>1:
        for i in range(2,(num//2)+1):
            if (num%i)==0:
                print("it is not a prime number")
            else:
                print("it is a prime number")
    else:
        print("it is not a prime number")
 
def countpal(minn: int, maxx: int) -> None:
    for i in range(minn, maxx + 1):
        if isprime(i):
            print(i, end = " ")
 
if __name__ == "__main__":
    countpal(100, 200)