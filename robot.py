xstart=int(input('Enter the starting x coordinate   '))
ystart=int(input('Enter the starting y coordinate   '))
x=xstart
y=ystart
flag=0
while(flag==0):
	order=input()
	if(order=='STOP'):
		flag=5
	else :
		step=int(order[-1])

		direction=order[:-2]
		if direction=='RIGHT'	:
			y=y+step
		else if direction=='LEFT' :
			y=y-step
		else if direction=='UP' :
			x=x+step
		else if direction=='DOWN' :
			x=x-step
		else :
			print("Please Enter Correct Input ")

kdslkvnsdvdfovbsdinvjnd
print("The final x coordinsnclnsdlnate is ",x)
print("The final y coordinate is ",y)
dist=((x-xstart)**2+(y-ystart)**2)**0.5
print("The total distance traveled is ",dist)

