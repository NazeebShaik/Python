n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0 and j<=n//2)or (j==n//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
