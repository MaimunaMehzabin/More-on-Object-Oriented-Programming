class Employee:
    def __init__(self):
         print("Employee created")
         
    def __del__(self):
        print("Destructor called")
        
def createObj():
    print("Making an onject")
    print()
    
    obj = Employee()
    print()
    
    return obj

print("Calling createObj() function")

obj = createObj()

print("Program end")
print()