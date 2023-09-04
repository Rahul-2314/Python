# fibonacci sum program
def fibo(n):
    if (n<=0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

def fibo_sum(n):
    if n<=0:
        return 0
    
    fib_sum=0

    for i in range(0,n):
        fib_sum+=fibo(i)
    
    return fib_sum

num=int(input("enter your number :"))

ans=fibo_sum(num)
print("Your solution :")
