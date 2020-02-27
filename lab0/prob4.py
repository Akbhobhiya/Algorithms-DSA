n=int(input('Enter the size of Array:'))
list=[]
for i in range(n):
	a=int(input())
	list.append(a)
def bubble(list):
	for i in range(n):
		for j in range(n):
			if list[j]>list[i]:
				x=list[i]
				list[i]=list[j]
				list[j]=x
def selection(list):
	for i in range(n):
		p=list[i]
		for j in range(n):
			if list[j]>list[i]:
				x=list[i]
				list[i]=list[j]
				list[j]=x
def main():
	q=int(input('Enter 1 for bubble and 2 for selection sort:'))
	if q==1:
		bubble(list)
		print(list)
	elif q==2:
		selection(list)
		print(list)
	else:
		print('enter a correct choice')
main()