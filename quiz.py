'''
   
'''
mark_list_database={}
mark_count=0
def qustionset(username,mark_list_database,mark_count):
    print("\n A.what is full form of HTML?? \n")
    print("1.hypertext youtube")
    print("2.hypuer uytij")
    print("3.lipun is best")
    print("4.hypertext markup language")
    
    answerkey=int(input("enter the answer: "))
    
    if(answerkey==4):
        mark_count=mark_count+1
        
    print("\n B.what is full form of CSS?? \n")
    print("1.cascading style sheet")
    print("2.cascading stylish sheet")
    print("3.caddaing stylish shheet")
    print("4.concataing stylish sheet")
    
    answerkey=int(input("enter the answer: "))
    
    if(answerkey==1):
        mark_count=mark_count+1

    print("\n C.what is full form of JS?? \n")
    print("1.java single")
    print("2.javascript")
    print("3.javasingular")
    print("4.javasinging")
    
    answerkey=int(input("enter the answer: "))
    
    if(answerkey==2):
        mark_count=mark_count+1
        
    
    mark_list_database[username]=f"mark is {mark_count}"
     
dict={}
password_list=[]
namelist=[]
while True:
    print("QUIZ APP")
    print("1.REGISTER")
    print("2.APPLY TEST")
    print("3.SCORE BOARD")
    
    
    choice=int(input("enter choice: "))
    if(choice==1):
       name=input("Enter your name : ")
       school=input("School name: ")
       number=int(input("Phone-number: "))
       password=int(input("Enter your exam password: "))
       
       if(password in password_list):
           print("Very similar password !please try  another one...")
            
       else:
            dict[name]=[school,number,password]
            print("\n Student registration completed successfully \n")
            password_list.append(password)
            namelist.append(name)
            
            
    elif(choice==2):
        username=input("Enter your name: ")
        check_password=int(input("Enter your pass: "))
        check_list_student=dict.get(username)
        
        if(username in namelist and check_password in check_list_student):
           qustionset(username,mark_list_database,mark_count)
           
        else:
           print("Your password is incorrect!!!")
           qus_pass=input("Are you want to see your login details: ")
           
           if(qus_pass=="yes"):
               username=input("Enter your name to verify: ")
               check_phone=int(input("Enter your number for verify: "))
               check_list_student=dict.get(username)
               if(username in namelist and check_phone in check_list_student):
                   print(dict[username])
               else:
                   print("soorry you again give the incorrect information")
           elif(qus_pass=="no"):
               print("ok try again with your coorect pass")
                
                
    elif(choice==3):
       print("WELCOME TO STUDENT MARK DATABASE")
       print(mark_list_database)
           
        
        
