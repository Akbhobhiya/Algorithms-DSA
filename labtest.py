
time=0
start=[0,0,0,0,0,0,0,0]
end=[0,0,0,0,0,0,0,0]
pred=[0,0,0,0,0,0,0,0]
def EC(G,visited,u):
    visited[u]=1
    start[u]=time+1
    sst=start[u]
    for v in G[u]:
        if visited[v]==0:
            sst=min(EC(G,visited,v),sst)
            pred[v]=u
        elif pred[u]!=v:
            sst=min(start[v],sst)
        if(start[u]==sst and sst!=0):
            print("bridges are:",v,pred[v])

    return sst
def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 
    visited=[0,0,0,0,0,0,0,0]
    '''for i in visited:
        visited[i]=0'''
    file=open('input1.txt','r')
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
    EC(G,visited,1)
    print(G)

if __name__ == '__main__':
    main()