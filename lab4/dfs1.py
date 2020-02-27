time=0
G=[]
file=open('input.txt','r')
for line in file:
    line=line.strip()
    adjacentVertices = []
    first=True
    for node in line.split(' '):
        if first:
            first=False
            continue
        adjacentVertices.append(int(node))
    G.append(adjacentVertices)

file.close()
def dfs(u):
    global time
    global st,ft,pred,visit
    visit[u]=1
    st[u]=time
    time+=1
    for v in G[u]:
        if visit[v]==0:
            pred[v]=u
            dfs(v)
            treeedge.append([u,v])
        else:
            if pred[u]!=v:
                backedge.append([u,v])
    ft[u]=time
    time+=1
st=[0 for i in range(len(G))]
ft=[0 for i in range(len(G))]
pred=[0 for i in range(len(G))]
visit=[0 for i in range(len(G))]
backedge=[]
treeedge=[]
u=int(input("enter source vertex:"))
dfs(u)
for i in range(len(G)):
    print("vertex",i,":",st[i],ft[i])
print("tree-edges : ",treeedge)
print("back-edges : ",end="")
for i in backedge:
    if i[0]>i[1]:
        print(i,end="")
print()