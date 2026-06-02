# f= open("practice.txt","w")

# f.write("Hi everyone \nwe are learning File I\O \nusing java \nI like programming in java")



# with open("practice.txt","r") as f :
 
#  data = f.read()

# new_data = data.replace("java","Python") 

# # print(new_data)

# with open("practice.txt","w") as f :
 
#  f.write(new_data)

# def check_word():
#  word = "learning"
#  with open("practice.txt","r") as f :
#     data = f.read()
#     if (data.find(word) != -1):
#      print("FOUND")
#     else :
#      print("NOT FOUND")


# check_word()




# def check_line() :
#   word = "Python"
#   data = True
#   line_num =1
#   with open("practice.txt","r") as f :
#       while True :
#         dataz = f.readline()
#         if(word in dataz):
#          print(line_num)
#          return                             #no return is NONE
#         line_num += 1
#   return -1

# print(check_line())    
  




# with open("practice.txt","r") as f :
#     data=f.read()
#     count =0
#     for i in data:
#         if (i%2==0):
#          count += 1

# print(count)







with open("practice.txt","r") as f :
    data=f.read()
    count=0
    nums=data.split(",")
    for val in nums:
        if (int(val)%2==0):
            count += 1

print(count)            