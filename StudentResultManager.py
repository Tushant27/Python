student = {}


while True :
    print ("\n------STUDENT RESULT MANAGER------")
    print ("1.Add student")
    print ("2.View student")
    print ("3.View result")
    print ("4.Exit")

    choice = (input("Enter your choice "))

    #Add student
    if choice == "1":
       name = input("enter name ")
       mark = int(input("enter mark "))
       student[name] = mark
       print (f"{name} Succesfully added")

    #View student
    elif choice == "2":
        if not student:
            print("No student found")
        else:
         for name , mark in student.items():
            print (name , " " ,mark)
             
    #View mark
    elif choice == "3":
       name = input("enter name : ")

       if name in student :
          mark = student[name]

          if mark<=40:
           print("FAIL")
          else:
             print("PASS")

       else:
          print("Student not present")

    #exit
    elif choice == "4":
       print("Exiting....")
       break
    else :
       print("invalid")  
     
       
        
      
          
