# class Student():

#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def get_avg(self):
#         sum=0
#         for val in self.marks :
#             sum += val
#         print("AVG :",sum/3)
         

# s1 = Student("Honey",[99,98,97]) 
# s1.get_avg()      


class Bank : 

    def __init__(self,accno,balance):
       self.accno = accno
       self.balance = balance

    def debit(self,amount):
        self.balance -= amount
        print("debited : " ,self.balance)


    def credit(self,amount):
        self.balance += amount
        print("credited : ",self.balance)

    def bal(self):
        print("Balance : ", self.balance)

acc1 = Bank(123,1000)
print(acc1.accno,acc1.balance)
acc1.bal()







