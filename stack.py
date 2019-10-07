stack=list()
top=-1
def push_element(stack,top):
	ch='Y'
	while ch=='Y' or ch=='y' or ch=='Yes':
		val=input("Enter the value to be added into the stack")
		stack.append(val)
		top+=1
		print('do you want to add more...<y/n>')
		ch=input()
		if ch=='N' or ch=='n' or ch=="No" or ch=="NO":
			break
	return top
