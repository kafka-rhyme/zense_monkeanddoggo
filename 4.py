while(1):
    n=int(input())
    l=[]
    for i in range(n):
        l.append(int(input()))

    sum=0
    for j in l:
         sum=sum+(j+j)
    print(sum)
    p=input()
    if(p=='n'):
       break
    else:
       continue
    
