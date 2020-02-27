from collections import deque
def bfs(src,prev,color,dist,G):
    color[src]=1
    prev[src]=-1
    dist[src]=0

    vis=[]
    queue = deque([src])
    while(queue):
        vertex=queue.popleft()
        print(vertex)
        vis.append(vertex)
        for u in G[vertex]:
            if color[u]==0:
                queue.append(u)
                prev[u]=vertex
                color[u]=1
                dist[u]=dist[vertex]+1





def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 
    prev=[]
    color=[]
    dist=[]
    inf=1000000000
    num=0
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
        num=num+1
    file.close()

    print(G)

   # src=int(input('Enter the source vertex'))
    cnt=1
    for i in range(num):
        if color[i]==0:
            print('Connected Component->',cnt)
            bfs(i,prev,color,dist,G)
            cnt=cnt+1





if __name__ == '__main__':
    main()