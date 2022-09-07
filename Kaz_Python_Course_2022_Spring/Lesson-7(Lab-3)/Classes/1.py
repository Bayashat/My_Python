class Task1:
    def getstring(self, string):
        self.name = string
    
    def printString(self):
        s = self.name.upper()
        print(s)

abc = Task1()

abc.getstring("apple")
abc.printString()