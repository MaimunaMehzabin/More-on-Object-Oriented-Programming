class IOString:
    
    def __init__(self):
        self.str1 = ""
        
    def get_String(self):
        self.str1 = input("Enter String : ")
        
    def print_string(self):
        print("Result is: ", self.str1.upper())
        

word1 = IOString()

word1.get_String()
word1.print_string()