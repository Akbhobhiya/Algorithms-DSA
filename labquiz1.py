
G=[]
file=open('input1.txt','r')
for line in file:
    line=line.strip()
    adjver=[]
    first=True
    for node in line.split(' '):
        if first:
            first=False
            continue
        adjver.append(int(node))
    G.append(adjver)
file.close()

time=0
pred=[0 for i in range(len(G))]
vi=[0 for i in range(len(G))]
start=[0 for i in range(len(G))]
def EC(u):
    global time
    vi[u]=1
    start[u]=time
    time+=1
    sst=start[u]
    for v in G[u]:
        if vi[v]==0:
            pred[v]=u
            sst=min(EC(v),sst)
        else:
            if pred[u]!=v:
                sst=min(sst,start[v])
    if (start[u]==sst and sst!=0):
        print("bridge edge is connected between (",u,",",pred[u],")")
    return sst
EC(0)
