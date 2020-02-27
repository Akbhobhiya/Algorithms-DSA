from collections import deque
def bfs(src,prev,color,dist,G):
    color[src]=1
    prev[src]=-1
    dist[src]=0

    vis=[]
    queue = deque([src])
    while(queue):
        vertex=queue.popleft()
        vis.append(vertex)
        for u in G[vertex]:
            if color[u]==0:
                queue.append(u)
                prev[u]=vertex
                color[u]=-color[vertex]
                dist[u]=dist[vertex]+1
            else:
                if color[u]== color[vertex]:
                    return False

    return True
def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 
    prev=[]
    color=[]
    dist=[]
    inf=1000000000
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
        prev.append(-1)
        color.append(0)
        dist.append(inf)
    file.close()

    print(G)

    if bfs(0,prev,color,dist,G)==True:
        print('Graph is Bipartite')
    else:
        print('Graph is not bipartite')




if __name__ == '__main__':
    main()