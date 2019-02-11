tup=(1,3,5,6,94,100,7)
for i in tup:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)