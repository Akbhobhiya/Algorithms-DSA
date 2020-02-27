from collections import deque 
def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 
    dist=[]
    prev=[]
    color=[]
    inf=100000
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
        dist.append(inf)
        color.append("white")
        prev.append(-1)
    file.close()
    print(G)
    s=int(input("enter the source vertex"))
    bfs(G,s,dist,color,prev)
def bfs(G,s,dist,color,prev):
    color[s]="gray"
    dist[s]=0
    de = deque([s])
    while de:
        u=de.popleft()
        print("vertex=",u, "  dist=",dist[u])
        for v in (G[u]):
            if color[v]=="white":
                color[v]="gray"
                dist[v]=dist[u]+1
                prev[v]=u
                de.append(v)
            color[u]="black"

if __name__ == '__main__':
    main()