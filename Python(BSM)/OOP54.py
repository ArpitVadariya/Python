class Parent:
    parentAttr = 100
    def __init__(self):
        print ("parent constructor called")
    def parentMethod(self):
        print('parent method called')
    def setAttr(self, attr):
        self.parentAttr = attr
    def getAttr(self):
        print("Parent attribute :", self.parentAttr)


class Child(Parent):
    def __init__(self):
        print ("child constructor called")
    def childMethod(self):
        print ('child method called')

c = Child() 
c.childMethod()  
c.parentMethod()  
c.setAttr(200)   
c.getAttr()