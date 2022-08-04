
def main():
    print("\n")
    print('''Welcome ,Here i Will be testing your G.K
Select Your Area Of interst''')
    print("\n")
    print("Choose Your Number \n1 Achievements  \n2 Geography \n3 Current Affairs \n4 to exit")
    ok()
    
Score=0

def ok():
    print("\n")
    choice =input()
    while True:
        if choice=="1":
            Achievements()
        if choice=="2":
              Geography()
        if choice=="3":
             CurrentAffairs()
        if choice=="4":
            print("Thank You,Bye")
            quit()     
                
def ChecktheAnswer(value):
    global Score    # Global variable:
    if value==True:
        Score+=1
    else:
        Score-=1
    return Score    
 

def Achievements():
    
    print("Q1) Who invented The Electric Bulb \n1. Edison  \n2.Girish \n3.Alok \n4.raju")
    print("\n")
    answer1=input("Enter your choice: ")
    if answer1=="1":
        ChecktheAnswer(True)
        print("Correct Answer")
    else :
        ChecktheAnswer(False)
        print("wrong answer")
        
    print("your Score is ",Score)
    
    print("\n")
    print("Q2) Who invented The  plane  \n1. Edison  \n2.Wright \n3.Alok \n4.raju")
    answer2=input("Enter your choice: ")
    if answer2=="2":
        ChecktheAnswer(True)
        print("Correct Answer")
    else :
        ChecktheAnswer(False)
        print("wrong answer")
    print("your Score is ",Score)
    
    print("\n")    
    print("Q3) Who invented The Amrita  \n1. Edison  \n2.Girish \n3.Amma \n4.raju")
    answer3=input("Enter your choice: ")
    if answer3=="3":
        ChecktheAnswer(True)
        print("wrong answer")
    else :
        ChecktheAnswer(False)
        print("wrong answer")
    print("your Score is ",Score) 
    print("\n")
    partover()

def Geography():
    
    print("Q1) Who invented The Electric Bulb \n1. Edison  \n2.Girish \n3.Alok \n4.raju")
    print("\n")
    answer1=input("Enter your choice: ")
    if answer1=="1":
        ChecktheAnswer(True)
        print("Correct Answer")
    else :
        ChecktheAnswer(False)
        print("wrong answer")
        
    print("your Score is ",Score)
    
    print("\n")
    print("Q2) Who invented The  plane  \n1. Edison  \n2.Wright \n3.Alok \n4.raju")
    answer2=input("Enter your choice: ")
    if answer2=="2":
        ChecktheAnswer(True)
        print("Correct Answer")
    else :
        ChecktheAnswer(False)
        print("wrong answer")
    print("your Score is ",Score)
    
    print("\n")    
    print("Q3) Who invented The Amrita  \n1. Edison  \n2.Girish \n3.Amma \n4.raju")
    answer3=input("Enter your choice: ")
    if answer3=="3":
        ChecktheAnswer(True)
        print("wrong answer")
    else :
        ChecktheAnswer(False)
        print("wrong answer")
    print("your Score is ",Score) 
    print("\n")
    partover()
    
def CurrentAffairs():
    print("Q1) Who invented The Electric Bulb \n1. Edison  \n2.Girish \n3.Alok \n4.raju")
    print("\n")
    answer1=input("Enter your choice: ")
    if answer1=="1":
        ChecktheAnswer(True)
        print("Correct Answer")
    else :
        ChecktheAnswer(False)
        print("wrong answer")
        
    print("your Score is ",Score)
    
    print("\n")
    print("Q2) Who invented The  plane  \n1. Edison  \n2.Wright \n3.Alok \n4.raju")
    answer2=input("Enter your choice: ")
    if answer2=="2":
        ChecktheAnswer(True)
        print("Correct Answer")
    else :
        ChecktheAnswer(False)
        print("wrong answer")
    print("your Score is ",Score)
    
    print("\n")    
    print("Q3) Who invented The Amrita  \n1. Edison  \n2.Girish \n3.Amma \n4.raju")
    answer3=input("Enter your choice: ")
    if answer3=="3":
        ChecktheAnswer(True)
        print("wrong answer")
    else :
        ChecktheAnswer(False)
        print("wrong answer")
    print("your Score is ",Score) 
    print("\n")
    partover()

        
def partover():   
    print("would like to try Another Topics")
    print("Type \"Yes\" Or \"No\" ")
    user=input()
    if user=="Yes":
        main()
    elif user=="No":
        quit()
    else:
        print("Type Correctly")
        partover()
        print("\n")
 
main()