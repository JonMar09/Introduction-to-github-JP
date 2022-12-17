class cal():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        return self.a-self.b
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
obj=cal(a,b)
operation=1
while operation!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation=int(input("Select Operation: "))
    if operation==1:
        print("Result: ",obj.add())
    elif operation==2:
        print("Result: ",obj.sub())
    elif operation==3:
        print("Result: ",obj.mul())
    elif operation==4:
        print("Result: ",round(obj.div(),2))
    elif operation==0:
        print("Exiting!")
    else:
        print("Invalid selection!!")
 
 
print()
