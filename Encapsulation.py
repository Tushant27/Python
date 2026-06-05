class A :
    _a = 10
    __b =100
    def tt(self):
        print(self._a)
        print(self.__b)


Obj = A() 
Obj.tt()
print(A._a)  
# print(A.__b)     
     