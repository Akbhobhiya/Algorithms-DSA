n=int(input('Enter the value of n:'))
list=[1,1]
def feb1(n):
	for i in range(2,n):
		list.append(list[i-1]+list[i])
def feb2(n):
	if n==1:
		return 1
	elif n<=0:
		return 0
	else:
		return feb2(n-1)+feb2(n-2)
def main():
	for i in range(1,n+1):
		print(feb2(i))
	print(list)
main()