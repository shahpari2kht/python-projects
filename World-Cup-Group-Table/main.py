
u=[]
Iran=[]
Spain=[]
Portugal=[]
Morocco=[]
I=[]
P=[]
S=[]
M=[]
dic={}
for i in range(6):
    fin=input()
    x=fin.split('-')
    u.append(x)
    
# Iran-Spain
if int(u[0][0])>int(u[0][1]):
    Iran.append('win')
    Spain.append('lose')
    I.append(int(u[0][0])-int(u[0][1]))
    S.append(-(int(u[0][0])-int(u[0][1])))
elif int(u[0][1])>int(u[0][0]):
    Iran.append('lose')
    Spain.append('win')
    S.append(int(u[0][1])-int(u[0][0]))
    I.append(-(int(u[0][1])-int(u[0][0])))
else:
    Iran.append('draw')
    Spain.append('draw')
    I.append(0)
    S.append(0)
    
# Iran-portugal
if int(u[1][0])>int(u[1][1]):
    Iran.append('win')
    Portugal.append('lose')
    I.append(int(u[1][0])-int(u[1][1]))
    P.append(-(int(u[1][0])-int(u[1][1])))
    
elif int(u[1][1])>int(u[1][0]):
    Iran.append('lose')
    Portugal.append('win')
    P.append(int(u[1][1])-int(u[1][0]))
    I.append(-(int(u[1][1])-int(u[1][0])))
else:
    Iran.append('draw')
    Portugal.append('draw')
    I.append(0)
    P.append(0)
    
# Iran-Morocco
if int(u[2][0])>int(u[2][1]):
    Iran.append('win')
    Morocco.append('lose')
    I.append(int(u[2][0])-int(u[2][1]))
    M.append(-(int(u[2][0])-int(u[2][1])))
elif int(u[2][1])>int(u[2][0]):
    Iran.append('lose')
    Morocco.append('win')
    M.append(int(u[2][1])-int(u[2][0]))
    I.append(-(int(u[2][1])-int(u[2][0])))
else:
    Iran.append('draw')
    Morocco.append('draw')
    I.append(0)
    M.append(0)
    
# Spain-Portugal
if int(u[3][0])>int(u[3][1]):
    Spain.append('win')
    Portugal.append('lose')
    S.append(int(u[3][0])-int(u[3][1]))
    P.append(-(int(u[3][0])-int(u[3][1])))
    
elif int(u[3][1])>int(u[3][0]):
    Spain.append('lose')
    Portugal.append('win')
    P.append(int(u[3][1])-int(u[3][0]))
    S.append(-(int(u[3][1])-int(u[3][0])))
else:
    Spain.append('draw')
    Portugal.append('draw')
    S.append(0)
    P.append(0)

#Spain-Morocco
if int(u[4][0])>int(u[4][1]):
    Spain.append('win')
    Morocco.append('lose')
    S.append(int(u[4][0])-int(u[4][1]))
    M.append(-(int(u[4][0])-int(u[4][1])))
    
elif int(u[4][1])>int(u[4][0]):
    Spain.append('lose')
    Morocco.append('win')
    M.append(int(u[4][1])-int(u[4][0]))
    S.append(-(int(u[4][1])-int(u[4][0])))
else:
    Spain.append('draw')
    Morocco.append('draw')
    M.append(0)
    S.append(0)
    
#Portugal-Morocco
if int(u[5][0])>int(u[5][1]):
    Portugal.append('win')
    Morocco.append('lose')
    P.append(int(u[5][0])-int(u[5][1]))
    M.append(-(int(u[5][0])-int(u[5][1])))
elif int(u[5][1])>int(u[5][0]):
    Portugal.append('lose')
    Morocco.append('win')
    M.append(int(u[5][1])-int(u[5][0]))
    P.append(-(int(u[5][1])-int(u[5][0])))
else:
    Portugal.append('draw')
    Morocco.append('draw')
    P.append(0)
    M.append(0)
   
#Iran

II=[]
winI=0
loseI=0
drawI=0
sumI=0
for k in Iran:
    if k=='win':
        winI+=1
    elif k=='lose':
        loseI+=1
    elif k=='draw':
        drawI+=1
    else:
        drawI=0
        winI=0
        loseI=0
for i in range(0,len(I)):
    sumI+=int(I.pop())
    
II.append(winI)
II.append(loseI)
II.append(drawI)
II.append(sumI)
II.append(3*winI+drawI)

#Spain
SS=[]
winS=0
loseS=0
drawS=0
sumS=0
for k in Spain:
    if k=='win':
        winS+=1
    elif k=='lose':
        loseS+=1
    elif k=='draw':
        drawS+=1
    else:
        drawS=0
        winS=0
        loseS=0
for i in range(0,len(S)):
    sumS+=int(S.pop())
    
SS.append(winS)
SS.append(loseS)
SS.append(drawS)
SS.append(sumS)
SS.append(3*winS+drawS)


#Portugal
PP=[]
winP=0
loseP=0
drawP=0
sumP=0
for k in Portugal:
    if k=='win':
        winP+=1
    elif k=='lose':
        loseP+=1
    elif k=='draw':
        drawP+=1
    else:
        drawP=0
        winP=0
        loseP=0
for i in range(0,len(P)):
    sumP+=int(P.pop())
    
PP.append(winP)
PP.append(loseP)
PP.append(drawP)
PP.append(sumP)
PP.append(3*winP+drawP)

#Morocco
MM=[]
winM=0
loseM=0
drawM=0
sumM=0
for k in Morocco:
    if k=='win':
        winM+=1
    elif k=='lose':
        loseM+=1
    elif k=='draw':
        drawM+=1
    else:
        drawM=0
        winM=0
        loseM=0
for i in range(0,len(M)):
    sumM+=int(M.pop())
    
MM.append(winM)
MM.append(loseM)
MM.append(drawM)
MM.append(sumM)
MM.append(3*winM+drawM)

dic['Iran']=II
dic['Spain']=SS
dic['Portugal']=PP
dic['Morocco']=MM
dct=sorted(sorted(dic.items(), key = lambda x : x[0]), key = lambda x : (x[1][4], x[1][0]), reverse = True)
for a,b in dct:
        print("{}  wins:{} , loses:{} , draws:{} , goal difference:{} , points:{}".format(a, b[0], b[1], b[2], b[3], b[4]))
