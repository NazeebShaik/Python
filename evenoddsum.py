li=list(map(int,input().split()))
esum=0
osum=0
for num in li:
    if num%2==0:
        esum+=num
    else:
        osum+=num
print(osum,esum)
        
