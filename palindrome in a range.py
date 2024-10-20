def isPalindrome(n: int) -> bool:
 
    rev = 0
    temp = n
    while temp> 0:
        rev = rev * 10 +temp % 10
        temp //= 10
 
    return (n == rev)
 
def countPal(minn: int, maxx: int) -> None:
    for i in range(minn, maxx + 1):
        if isPalindrome(i):
            print(i, end = " ")
 
# Driver Code
if __name__ == "__main__":
    countPal(100, 2000)