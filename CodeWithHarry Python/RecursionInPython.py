def fib(n):
    if (n==0 or n==1):
        return n
    else:
        return(fib(n-2)+fib(n-1))
num = int(input("enter fib indx:"))
print(fib(num))