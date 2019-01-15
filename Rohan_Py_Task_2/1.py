n=int(input())
print(n)
if((n%2==1)or((n%2==0) and (6<=n<=20))):
    print("weird")
elif((n%2==0) and ((2<=n<=5)or(n>20))):
    print("not weird")