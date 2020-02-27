a=int(input('Enter the positive number for factorial:'))
def fac1(a):
    sum=1
    if a==0:
        return 1
    else:
        for i in range(1,a+1):
            sum=sum*i
        return sum
def fac2(a):
    if a==1:
        return 1
    elif a==0:
        return 1
    else:
        return a*fac2(a-1)

def main():
    print("factorial of", a ,"is", fac1(a))
    print("factorial of", a ,"is", fac2(a))
main()
