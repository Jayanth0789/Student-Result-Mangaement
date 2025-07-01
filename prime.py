def prime(n):
    for i in range(2,(n//2)+1):
        flag=0
        if n%i==0:
            flag = 1
            break
    if flag == 0:
        return "Prime"
    else:
        return "Not prime"

n = int(input("Enter a number: "))
print(prime(n))