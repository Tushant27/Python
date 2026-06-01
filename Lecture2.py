# str1='yoyo'
# str2="yoyo"
# str3="""yoyo"""

# print(str1,str2,str3)

# str4 = "Apple"

# print(str4[-3:-1])
# print(str4[0:2])


# print(str1.len())

# str = "i am a coder"

# print(str.capitalize())
# print(str)



# str = input("enter a string : ")
# print (len(str))
# print("$ occurance :" , str.count("$"))

# marks = int(input("enter your marks : "))
# if (marks>=90):
#     print("A")
# elif(marks<90 and marks>=80):  
#     print("B")
# elif(marks<80 and marks>=70):  
#      print("C")
    
# num = int(input("Enter a number :"))
# if (num%2==0):
#     print(num," is even")
# else : 
#     print(num," is odd")

num1 = int(input("Enter 1st number :"))
num2 = int(input("Enter 2nd number :"))
num3 = int(input("Enter 3rd number :"))

if (num1>num2 and num1>num3):
    print(num1, " is grestest")
if (num2>num1 and num2>num3): 
     print(num2, " is grestest")  
else :     
    print(num3, " is grestest")  
