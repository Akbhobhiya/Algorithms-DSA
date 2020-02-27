class Node:
    def __init__(self,x):
        self.val = x
        self.parent = self
        self.rank = 0

    def __str__(self):
        return str(self.val)

class DisjointSets:
	def makeset(self,x):
		node=Node(x)
		return node
	def union(self,x,y):
		rx=self.findset(x)
		ry=self.findset(y)
		if(rx==ry):
			return
		if(rx.rank>ry.rank):
			ry.parent=rx;
		else:
			rx.parent=ry
			if(rx.rank==ry.rank):
				ry.rank+=1
	def findset(self,x):
		root=x
		while root.parent!=root:
			root=root.parent
		current=x
		while current!=current.parent:
			parent=current.parent
			current.parent=root
			current=parent
		return root
   
def main():
    ds = DisjointSets()
    
    nodes = []
    for i in range(10):
        node = ds.makeset(i)
        nodes.append(node)

    ds.union(nodes[0],nodes[1])
    print(ds.findset(nodes[0]))    # Should print 1
    ds.union(nodes[0],nodes[2])
    print(ds.findset(nodes[2]))    # Should print 1
    ''' Add more tests!'''
    ds.union(nodes[2],nodes[3])
    print(ds.findset(nodes[3]))

if __name__ == '__main__':
    main()