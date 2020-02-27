a=int(input('Enter a number:'))
def prime(a):
	sum=0
	for i in range(1,a+1):
		if a%i==0:
			sum=sum+1
	if sum>2:
		return 0
	else:
		return 1
def main():
	x=prime(a)
	if x==1:
		print('TRUE')
	else:
		print('FALSE')
main()
