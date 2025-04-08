n=int(input())

vote={}
vote1=dict()

for i in range(n):
	s=input()	
	if s in list(vote.keys()):
		vote[s]+=1
	else:
		vote[s]=1

z=list(vote.keys())
z.sort()
for i in z:
	print(i,vote[i])
 