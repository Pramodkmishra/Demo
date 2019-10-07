stack=list()
top=-1
def push_element(stack,top):
	ch='Y'
	while ch=='Y' or ch=='y' or ch=='Yes':
		val=input("Enter the value to be added into the stack=")
		stack.append(val)
		top+=1
		print('do you want to add more...<y/n>:')
		ch=input()
		if ch=='N' or ch=='n' or ch=="No" or ch=="NO":
			break
	return top
def pop_element(stack,top):
	slen=len(stack)
	if slen<=0:
		print("Stack is empty.")
	else:
		val=stack.pop()
		top=top-1
		print("Value deleted from stack is=",val)
	return top
def show_element(stack,top):
	slen=len(stack)
	if slen<=0:
		print("Stack is empty.")
	else:
		print("The stack element are....")
		i=top
		while(i>=0):
			print(stack[i])
			i=i-1
while(True):
	print()
	print("Stack Operation")
	print("______________________")
	print("1.Adding Element to a stack")
	print("2.Removing Element from a stack")
	print("3.Showing Elements of a stack")
	print("4.Exit from stack")
	opt=int(input("Enter your option="))
	print()
	if opt==1:
		top=push_element(stack,top)
	elif opt==2:
		top=pop_element(stack,top)
	elif opt==3:
		show_element(stack,top)
	elif opt==4:
		break



Output:

Stack Operation
______________________
1.Adding Element to a stack
2.Removing Element from a stack
3.Showing Elements of a stack
4.Exit from stack
Enter your option=1

Enter the value to be added into the stack=100    
do you want to add more...<y/n>:
y
Enter the value to be added into the stack=350
do you want to add more...<y/n>:
y
Enter the value to be added into the stack=Delhi
do you want to add more...<y/n>:
y  
Enter the value to be added into the stack=210
do you want to add more...<y/n>:
y
Enter the value to be added into the stack=Chennai
do you want to add more...<y/n>:
y
Enter the value to be added into the stack=05-10-2019
do you want to add more...<y/n>:
y  
Enter the value to be added into the stack=560
do you want to add more...<y/n>:
n

Stack Operation
______________________
1.Adding Element to a stack
2.Removing Element from a stack
3.Showing Elements of a stack
4.Exit from stack
Enter your option=3   

The stack element are....
560
05-10-2019
Chennai
210
Delhi
350
100

Stack Operation
______________________
1.Adding Element to a stack
2.Removing Element from a stack
3.Showing Elements of a stack
4.Exit from stack
Enter your option=2

Value deleted from stack is= 560

Stack Operation
______________________
1.Adding Element to a stack
2.Removing Element from a stack
3.Showing Elements of a stack
4.Exit from stack
Enter your option=3

The stack element are....
05-10-2019
Chennai
210
Delhi
350
100

Stack Operation
______________________
1.Adding Element to a stack
2.Removing Element from a stack
3.Showing Elements of a stack
4.Exit from stack
Enter your option=2

Value deleted from stack is= 05-10-2019

Stack Operation
______________________
1.Adding Element to a stack
2.Removing Element from a stack
3.Showing Elements of a stack
4.Exit from stack
Enter your option=3

The stack element are....
Chennai
210
Delhi
350
100

Stack Operation
______________________
1.Adding Element to a stack
2.Removing Element from a stack
3.Showing Elements of a stack
4.Exit from stack
Enter your option=1

Enter the value to be added into the stack=Vikash
do you want to add more...<y/n>:
n

Stack Operation
______________________
1.Adding Element to a stack
2.Removing Element from a stack
3.Showing Elements of a stack
4.Exit from stack
Enter your option=3

The stack element are....
Vikash
Chennai
210
Delhi
350
100

Stack Operation
______________________
1.Adding Element to a stack
2.Removing Element from a stack
3.Showing Elements of a stack
4.Exit from stack
Enter your option=4


