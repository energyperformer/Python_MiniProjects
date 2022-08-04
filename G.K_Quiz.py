
print('''Welcome ,Here i Will be testing your G.K
Select Your Area Of interst''')
print("Choose Your Number \n1 Achievements  \n2 Geography \n3 Current Affairs \n4 to exit")
Option=int(input())
Score=0
if(Option==1):
    print("Your First Question is ")
    print("who invented Bulb")
    print("Choose Your Number \n1 Edison  \n2 Alok \n3 Rajendra \n4 to Girish")
    answer1=int(input())
    if(answer1==1):
        print("Correct")
        Score+=1
    else:
        print("Better Luck Next Time ")
        if (Score<=0):
            Score==0
        else:
            Score-=1
        
    print("who invented Bulb")
    print("your Current Score is ",Score)   
    
    print("your Second Question is ")
    print("Who Inveted Abgular Velocity")
    print("Choose Your Number \n1 Edison  \n2 Alok \n3 Newton \n4 to Girish")
    answer2=int(input)()
    if(answer2==3):
        print("Correct")
        Score+=1
    else:
       
        print("Better Luck Next Time ")
        if (Score<=0):
            Score==0
        else:
            Score-=1
        
        print("who invented Bulb")
    print("your Current Score is ",Score)       
        
    print('''your 3rd Question is
Who is God''')
    
    print("Choose Your Number \n1 Edison  \n2 Alok \n3 Rajendra \n4 to Girish")
    answer3=int(input)()
    if(answer3==4):
        print("Correct")
        Score+=1
    else:
        print("Better Luck Next Time ")
        Score-=1
    print("your Current Score is ",Score)
    
if(Option==4):
    print("Quiting")
    quit()
    