class A :
    @staticmethod
    def showA():
      
        print("class A")

class B(A):
    @staticmethod
    def showB():
     
        print("class B")

class C(B) :
    @staticmethod
    def showC():
        
        print("class C")       


c1 = C()  
c1.showA()
