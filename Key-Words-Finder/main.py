x = []
n = str(input())
n = n.replace(',', '')
n = n.replace("0", "").replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("0", "")
n = n.split('. ')
n[-1] = n[-1].replace(n[-1][-1], '')
#print(n)
for i in n:
    y = i.split()
    y[0] = 'q'
    x = x + y
#print(x)
z = []
for i in x:
    if i == i.capitalize():
        m = []
        m.append(x.index(i))
        m.append(i)
        x[x.index(i)] = 'q'
        z.append(tuple(m))
for i in range(len(z)):
    print(str(z[i][0]+1)+':'+z[i][1])
if z == []:
    print(None)
