
adList = [None] * 100
startTime = [None] * 100
finishTime = [None] * 100
pred = [None] * 100
time = 0
visited = [False] * 100
treeEdges = []
backEdges = []
sst = 0
source = 0



def twoEdge(u):
    global time
    global adList, startTime, finishTime, pred, visited, treeEdges
    startTime[u] = time
    time += 1 
    visited[u] = True
    sst = startTime[u]
    for v in adList[u]:
        if not visited[v]:
            treeEdges.append((u,v))
            pred[v] = u
            sst = min(twoEdge(v), sst)
        else:
            if pred[u] != v and startTime[u] > startTime[v]:
                sst = min(startTime[v], sst)
    finishTime[u] = time
    time += 1
    if u != source and sst == startTime[u]:
        print(f"exit at {u} and not edge connected")
        exit()
    return sst     



G = [] 
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




print(G)
adList = G
n = len(adList)
twoEdge(0)

