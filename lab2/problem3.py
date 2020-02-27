if __name__ == '__main__':
	a,b=input("enter the number of vertices and edges").split()
	a=int(a)
	b=int(b)
	m=[[0 for i in range(a)] for i in range(a)]
	l=[[] for i in range(a)]
	print("enter the edges")
	for i in range(b):
		x1,x2=input().split()
		x1=int(x1)
		x2=int(x2)
		m[x1][x2]=1
		m[x2][x1]=1
		l[x1].append(x2)
		l[x2].append(x1)
	print("the adjacency matrix is : ")
	for i in m:
		print(i)
	print("the adjacency list is : ")
	for i in range(a):
		print("vertex",i," : ",l[i])