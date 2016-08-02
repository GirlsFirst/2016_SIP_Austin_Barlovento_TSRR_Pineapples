import time, random

#0 = incomplete
#1 = complete
#The corresponding function will change this variable when the player has done everything for that area
friend_house_complete=0
docks_complete=0
playground_complete=0
school_complete=0

def end_area():
    print("You made it!")

def school():
    #Needs a check to make sure the player got everything before they leave
    print("You made it! 4")
    print("Now go back...")
    map()

def playground():
    #Needs a check to make sure the player got everything before they leave
    print("You made it! 3")
    print("Now go back...")
    map()

def docks():
    #Needs a check to make sure the player got everything before they leave
    print("You made it! 2")
    print("Now go back...")
    map()

def friend_house():
    #Needs a check to make sure the player got everything before they leave
    print("You made it! 1")
    print("Now go back...")
    map()

def map():
    print("")
    print("You look around.")
    print("Where will you go?")
    print("-----------------------------")
    print("[1]Friend's House (Easy Difficulty)")
    print("[2]Docks (Hard Difficulty)")
    print("[3]Playground (Medium Difficulty)")
    print("[4]School (Easy Difficulty)")
    print("[5]Quit")
    selected=input(">> ")

    if selected=="1":
        if friend_house_complete==1:
            print("I don't need to go here.")
            time.sleep(2)
            map()
        else:    
            print("You walk to your Friend's House")
            time.sleep(2)
            friend_house()
    elif selected=="2":
        if docks_complete==1:
            print("I don't need to go here.")
            time.sleep(2)
            map()
        else:    
            print("You walk to the Docks")
            time.sleep(2)
            docks()
    elif selected=="3":
        if playground_complete==1:
            print("I don't need to go here.")
            time.sleep(2)
            map()
        else:    
            print("You walk to the Playground")
            time.sleep(2)
            playground()
    elif selected=="4":
        if school_complete==1:
            print("I don't need to go here.")
            time.sleep(2)
            map()
        else:    
            print("You walk to the School")
            time.sleep(2)
            school()
    elif selected=="5":
        print("Are you sure you want to quit?")
        print("You might loose your progress.")
        print("[1]Yes")
        print("[2]No")
        selected=input(">> ")
    
        if selected=="1":
            print("Quitting...")
            time.sleep(2)
            quit()
        else:
            map()
    else:
        print("Invalid Input")
        print("")
        time.sleep(2)
        map()
        
    
def check(): #Checks to see if all locations are completed
    if (friend_house_complete==1 and docks_complete==1 and playground_complete==1 and school_complete==1):
        end_area()
    else:
        map()
        
def start_area(): #Tutorial!
        print("It's a bright and sunny morning, the birds are chirping like the amazing alarm clock they are and the flaming ball of    gas in the sky shines on your face through the cracks of the blinds.")
        time.sleep(2)
        print("You don't want to get out of bed but the insistent chirping keeps you from going back to sleep.")
        time.sleep(2)
        print("As you awake you notice the sweet morning breeze - or you would if you had been camping with the rest of the dorm.")
        time.sleep(2)
        print("Instead, you continue to hole yourself up in your room and continue writing.")
        time.sleep(2)
        print("Or you would if you hadn't been locked out of your computer.")
        time.sleep(2)
        print ("You desperately need to log back in, but you've forgotten your password as you never log out.")
        time.sleep(2)
        print("")
        print ("TUTORIAL")
        time.sleep(2)
        x=True #place holding variable
        while x==True:
            print("     ")
            print("What will you do?")
            print("-----------------------------")
            print("[1]Try a password")
            print("[2]Do nothing")
            selected=input(">> ")
        
            if selected=="1":
                print("You try a password")
                time.sleep(2)
                print("You're denied access")
                x=False
            elif selected=="2":
                print("You do nothing...")
                time.sleep(2)
        
        start_num=0 #Another place holding variable
        
        while (start_num<=2):
            time.sleep(2)
            print("")
            print("Now what?")
            print("-----------------------------")
            print("[1]Try again")
            print("[2]Try another password")
            selected=input(">> ")

            start_num=start_num+1
            
        remaining_guess=3
        
        while (remaining_guess>=0):
            time.sleep(2)
            print("")
            print("Growing ever irritated with you the computer displays a hint")
            print("Hint: Alice's Dog")
            selected=input("Enter a password: ")
            fixed_entry=selected.lower() #This puts the enter in all lowercase characters
            password="captain"
            
            if (fixed_entry == password):
                print("Your password is accepted")
                time.sleep(2)
                print("The Desktop opens")
                print("")
                print("TUTORIAL COMPLETE!")
                print("")
                check()
            else:
                remaining_guess=remaining_guess-1
            
            

def start_menu(): 
    print("-----------------------------")
    print("Game Title")
    print("-----------------------------")
    print("[1]Play")
    print("[2]Website Link")
    print("[3]Quit")
    selected=input(">> ")
    
    if selected=="1":
        print("Loading Game...")
        print("")
        time.sleep(2)
        start_area()
        
    elif selected=="2":
        print("Copy and Paste the link into your browser")
        print("Website Link")
        print("")
        print("Press any key to return to menu")
        selected=input()
        
        if selected=="1":
            print("Returning to menu...")
            print("")
            time.sleep(2)
            start_menu()
        else:
            print("Returning to menu...")
            print("")
            time.sleep(2)
            start_menu()
        
    elif selected=="3":
        print("Quitting...")
        time.sleep(2)
        quit()
        
    else:
        print("Invalid Input")
        print("")
        time.sleep(2)
        start_menu()
            
start_menu()

