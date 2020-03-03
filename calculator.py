def add(a,b):
	print(a+b)
def sub(a,b):
	print(a-b)
def mul(a,b):
	print(a*b)
def div(a,b):
	print(a/b)
class Calculator
	def add(self):
		print(a+b)
	def sub(self):
		print(a-b)
	def mul(self):
		print(a*b)
	def div(self):
		print(a/b)
a=int(input("Enter the first number\n"))
b=int(input("Enter the second number\n"))
obj=Calculator()
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.division)
ch=int(input("Enter your choice:"))
if ch==1:
	obj.add()
elif ch==2:
	obj.sub()
elif ch==3:
	obj.mul()
elif ch==4:
	obj.div()
else:
	print("wrong choice")
