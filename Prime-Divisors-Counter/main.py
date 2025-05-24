def prime(num):
    if(num==1):
        return 0
    for i in range(2,((num//2)+1)):
        if(num%i==0):
            return 0
    return num
num=[]
dic={}
u=[]
for i in range(10):
    l=int(input())
    num.append(l)
    for j in num:
        temp=0
        for x in range(1,j+1):
            if j%x==0:
                if (prime(x)!=0):
                    temp+=1
    dic[num[i]]=temp
tup=list((dic.items()))
max_ord=max(dic.values())
for r in range(0,len(tup)):
    q=(a,b)=tup.pop()
    if b==max_ord:
        u.append(q)
max_key=max(u)
a,b=max_key
print('%i %i'%(a,b))
