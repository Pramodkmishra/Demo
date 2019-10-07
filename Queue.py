queue=list()
rear=-1
def insert_queue(queue,rear):
	ch='y'
	while ch=='y' or ch=='Y' or ch=='Yes':
		val=input("Enter Element to be inserted=")
		rear+=1
		queue.append(val)
		ch=input("do you want to add more..<y/n>:")
		if ch=='N' or ch=='n' or ch=='No' or ch=="NO":
			break
	return rear
def remove_queue(queue,rear):
	qlen=len(queue)
	if qlen==0:
		print("Queue is empty")
	else:
		print("Deleted Element=",queue[0])
		del(queue[0])
		rear-=1
	return rear
def show_queue(queue,rear):
	qlen=len(queue)
	if qlen<=0:
		print("Queue is Empty:")
	else:
		print("Queue elemets are..")
		i=0
		while i<=rear:
			print(queue[i]," ",end="")
			i=i+1
while(True):
	print()
	print("Queue Operation")
	print("______________________")
	print("1.Adding element to a Queue")
	print("2.Removing element from a queue")
	print("3.Showing element of a queue")
	print("4.Exit from queue")
	opt=int(input("Enter your option="))
	print()
	if opt==1:
		rear=insert_queue(queue,rear)
	elif opt==2:
		rear=remove_queue(queue,rear)
	elif opt==3:
		show_queue(queue,rear)
	elif opt==4:
		break

