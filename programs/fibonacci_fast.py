# fibonacci series

def fibonacci(num):
    arr=[0,1]
    for i in range(num-2):
        sum = arr[-1]+arr[-2]
        arr.append(sum)
    return arr

def fibonacci_sum(ans):
    t=0
    for a in ans:
        t+=a
    return t

num = int(input("enter your number :"))

ans=fibonacci(num)
print("\nFibonacci Series :",ans)

sol=fibonacci_sum(ans)
print("\nYour Solution :",sol)
