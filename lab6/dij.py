import heapq
def main():
    G = []
    file=open('input.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        first=True
        for edge in line.split(' '):
            if first:
                first=False
                continue
            node,weight = edge.split(',')
            adjacentVertices.append((int(node),int(weight)))
        G.append(adjacentVertices)
    file.close()
    dist=[92312423]*len(G)
    pred=[0]*len(G)
    s=int(input('enter the source vertex::'))
    Dij(G,s,dist,pred)
    for i in range(len(dist)):
    	print("distance between (",s,",",i,") is:",dist[i])
def Dij(G,s,dist,pred):
	dist[s]=0
	H=[s]
	while len(H)!=0:
		u=heapq.heappop(H)
		for v in G[u]:
			if dist[v[0]]>dist[u]+v[1]:
				dist[v[0]]=dist[u]+v[1]
				heapq.heappush(H,v[0])
				pred[v[0]]=u

if __name__ == '__main__':
    main()