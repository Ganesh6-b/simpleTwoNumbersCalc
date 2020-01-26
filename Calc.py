val1 = int(input("Enter you number 1:"))
val2 = int(input("Enter you number 2:"))

def add(val1,val2):
    print("Addition of {} and {} is ".format(val1,val2), val1+val2)
def sub(val1,val2):
    print("Subraction of {} and {} is ".format(val1,val2),val1-val2)
def mul(val1,val2):
    print("Multiplication of {} and {} is ".format(val1,val2),val1*val2)
def div(val1,val2):
    print("Division of {} and {} is ".format(val1,val2),val1/val2)
print("Enter your operations:")
print("1:Add")
print("2:Subraction")
print("3:Multiply")
print("4:Division")

Operation = int(input("1/2/3/4:"))

if Operation==1:
    add(val1,val2)
elif Operation==2:
    sub(val1,val2)
elif Operation==3:
    mul(val1,val2)
elif Operation==4:
    div(val1,val2)
else:
    print("Enter the valid operation:")
