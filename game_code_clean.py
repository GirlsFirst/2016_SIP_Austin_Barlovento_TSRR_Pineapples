import time, random

#variables
#choice_puzzle = False

#0 = incomplete
#1 = complete
#The corresponding function will change this variable when the player has done everything for that area
friend_house_complete=False
docks_complete=False
playground_complete=False
school_complete=False

#**********Check**********

def check(): #Checks to see if all locations are completed
    #*side note: this doesn't appear when it runs
    global friend_house_complete
    global docks_complete
    global playground_complete
    global school_complete
    if (friend_house_complete  and  docks_complete  and  playground_complete  and  school_complete):
        end_area()
    else:
        map()

#**********End Area**********

def end_area():
    print("If you've decrypted the email, all four lines finally make sense.")
    time.sleep(2)
    print("If not, then decrypt the 5th message in your inbox from earlier.")
    location = ""
    while location  != "cabin by the woods":
        location = input("Where is Alice?")
        print(" ")
        location.lower()
        if location == "cabin by the woods":
               print("Desperate to finally find Alice, you walk towards the cabin by the woods.")
               time.sleep(2)
               print("You're anxious and, despite your eagerness, apprehensive because you don't know what you'll see.")
               time.sleep(2)
               print("The forest is damp, dark, and dreary, to a studious extent, not helping you at all.")
               time.sleep(2)
               print("As soon as you see the cabin, you dash to the door as though it will save you from the monsters of your imagination.")
               time.sleep(2)
               print("Then you realize the largest monster was probably in there.")
               print(" ")
               print("What do you do?")
               print("-----------------------------")
               print("[1]Kick down the door")
               print("[2]Knock on the door")
               selected=input(">> ")
               if selected=="1":
                    x=False
                    print("You kick down the door and debris goes flying, it was an old and week door anyway.")
                    time.sleep(2)
                    print("You look inside and see a computer running in the corner and a window when you look to the front.")
                    time.sleep(2)
                    print('''You hear a voice you don't recognize call out "WAIT", but you can't do much else after that.''' )
                    time.sleep(2)
                    print("Someone hits you hard on the back of the head, and you hit the floor, face first.")
                    time.sleep(2)
                    print('''"The last thing you hear before you black out is Alice's voice asking "Is s(he) dead?"''')
                    time.sleep(2)
                    print("THE END")
                    time.sleep(2)
                    print("If you want a better ending - try again.")
                    start_menu()
               elif selected=="2":
                   x=False
                   print("You knock on the door and wait for someone to open it.")
                   time.sleep(2)
                   print("You pray it's not a serial killer as the door creaks open just enough for the person inside to see you, but not the other way around.")
                   time.sleep(2)
                   print("Before you have the chance to see who it was that opened the door, the figure pounces on you.")
                   time.sleep(2)
                   print("It wraps it's arms around you in a giant hug.")
                   time.sleep(2)
                   print("It was Alice.")
                   time.sleep(2)
                   print('''OMGITHOUGHTYOUWOULDNEVERFINDUSANDITHOUGHTTHECLUESWERETOCRYPTICAND
              OMGOMGOMGOMGTHEPASSWORDISAPPLEYOUMADEITEVENTHOUGHITWASTOOHARDAND
              THEMESSAGESSHOULD'VEBEENMORESRAIGHTFORWARDBUTICOULD'TCONVINCEHER!!!!''')
                   time.sleep(2)
                   print(" ")
                   print("You don't understand a thing of what she is saying, but you are overly glad to see her.")
                   time.sleep(2)
                   print ("You think everything is going to be okay, but just as you do, you see a silhouette creep up behind Alice.")
                   time.sleep(2)
                   print("THE END")
                   print(" ")
                   print("If you would like to read the complete ending, please enter the password at the menu.")

#**********Playground puzzle 2**********

def playground_puzzle_2():
    print('''You see a sketch under the note, with x's on a map. Under the map was "X marks the spot"''')
    time.sleep(2)
    print("The x's on the map coordinate to various items placed in the sandbox.")
    time.sleep(2)
    print(" ")
    time.sleep(2)
    print("[1] Dig under the pail")
    print("[2] Dig under the shell")
    print("[3] Dig under the pony")
    print("[4] Dig under the shovel")
    print("[5] Dig under the stuffed animal")
    print(" ")
    selected = ""
    while selected != "3":
        print("What do you dig up?")
        selected=input(">> ")
        if selected == "3":
            print("You dig under the item and find a calender")
            print("The calender is very similar to the one on the blog, it has an x on the 12th of March.") #Filler
            time.sleep(2)
            print(" ")
            # playground_complete=True
            check()
        else:
            print("You find nothing but little bits of useless trash.")

#**********Playground puzzle 1**********

def playground_puzzle_1():
    print("You go to the playground in order to check for anything - as if they could hide anything there.")
    time.sleep(2)
    print("Although you know better, you still expect the giant colorful world you saw when you were younger.")
    time.sleep(2)
    print("Instead you get the faded-to-gray and tiny playground of your neighborhood.")
    print(" ")
    time.sleep(2)
    print("It's not the first time you've seen it like this - but today it felt especially bare.")
    time.sleep(2)
    print("You glance over the area, not expecting anything, but you catch a note on the swings.")
    time.sleep(2)
    print("Resisting the temptation to sit on the swing set, you look at the note.")
    time.sleep(2)
    print("The note says:")
    time.sleep(2)
    print("What doesn't kill you makes you stronger - think about your childhood memories.")
    time.sleep(2)
    selected=""
    while selected != "monkey bars" or  selected  != "monkeybars":
        print("A childhood memory was shared here.")
        print("Do you remember where it was? ")
        print("-----------------------------")
        selected=input(">> ")
        if selected == "monkey bars" or  selected  == "monkeybars" :
            print(" ")
            print("You remember about when Alice broke her arms on the monkey bars, and head over to them.")
            print("On the side handle, you see enother note referring you to the sandbox.")
            print(" ")
            time.sleep(2)
            playground_puzzle_2()
        else:
            print("No that wasn't the location the note referred to.")
#********Playground********
def playground():
    global playground_complete
    playground_complete = True
    playground_puzzle_1()
    

    
#**********School puzzle 2**********

def school_puzzle_2():
    selected = "" #Place Holder
    print ("You open the locker and look inside to see Alice's old computer - the ONE that sill worked.")
    time.sleep(2)
    print("As you seem to have a bad rep with technology - the computer is locked.")
    time.sleep(2)
    print("You try every password of hers you know yet again, but none of them actually work.")
    time.sleep(2)
    print("Your knack to frustrate computers is strong, so the computer displays another hint.")
    print(" ")
    while selected != "your name":
        print("What is yours to own, yet others use it more?")
        print("Enter the passowrd")
        print("-----------------------------")
        selected = input(">> ")
        if selected == "your name":
            print(" ")
            print("The computer unlocks and displays a screen fill with only dots and dashes, and nothing else works.")
            time.sleep(2)
            print(" ")
            print("The screen displays:.... .")
            time.sleep(2)
            # chool_complete=True
            check()
        else:
            print("That is not the correct passowrd.")

#**********School puzzle 1**********

def school_puzzle_1():
    x=True #Place Holder
    correct_num1="22"
    correct_num2="3"
    correct_num3="34"
    
    print("The rooms and the 10-20 lockers had combination locks that the students and teachers brought in.")
    time.sleep(2)
    print("The only thing here that could possibly relate to Alice is her locker, so you make your way over there.")
    time.sleep(2)
    print("The locker still had a lock on it. The warmth of the metal tells you someone was there, though it had been a while since they left.")
    time.sleep(2)
    print(" ")
    print("You proceed to unlock the mechanism, using Alice's blog as a reference.")
    print("*enter the numbers one at a time")
    print("-----------------------------")
    while x==True:
        print("Enter the first number")
        num1=input(">> ")
        print("Enter the second number")
        num2=input(">> ")
        print("Enter the third number")
        num3=input(">> ")
        
        print("")
        print("You enter the code ...")
        print("")
        if num1==correct_num1:
            print("You hear a click indicating that the first number is correct")
            if num2==correct_num2:
                print("You hear a second click, indicating that the second number is correct.")
                if num3==correct_num3:
                    print("That's it!")
                    time.sleep(2)
                    print("The lock opens")
                    school_puzzle_2()
                    x=False
                else:
                    print("Nope, that isn't it.")                   
            else:
                print("Nope, that isn't it.")        
        else:
            print("Nope, that isn't it.")

#**********School**********

def school():  
    print("You reach school with a sinking pit in your stomach.")
    time.sleep(2)
    print("It didn't mean something bad was going to happen - it was just a premonition of going to school.")
    time.sleep(2)
    print("You had a few fond memories of the place, but you were glad you were only visiting.")
    print(" ")
    time.sleep(2)
    print("With no children in town, the school ended up shutting down, so there was no one there.")
    time.sleep(2)
    print("You manage to get into the school building by climbing the fence.")
    time.sleep(2)
    print("The doors had no locks. The small amount of children in town made it hard to maintain due to lack of funds.")
    time.sleep(2)
    global school_complete
    school_complete = True
    school_puzzle_1()
    

#**********Docks puzzle 2**********

def dock_puzzle_2():
    choice_puzzle = "" #Place Holder
    print("   ")
    print("As you walk towards the dock you finally experience the cool air, freshwater smell, and the sound of moving water you had been waiting for.")
    time.sleep(2)
    print("You see an expansive lake before you.")
    time.sleep(2)
    print("There is a small fishing boat to your right and in front of it is a tackle box and fishing pole.")
    print(" ")
    time.sleep(2)
    print("Alice was afraid of ships, and since so far this had all been related to Alice's better memories, you knew no hints would be found there.")
    time.sleep(2)
    print("Instead you look at the tackle box, which is had a small number lock on it.")
    time.sleep(2)
    while  choice_puzzle != "692":
        print(" ")
        print("What is the code to the tackle box?")
        print("*it's a 3 digit number")
        print("-----------------------------")
        choice_puzzle= input(">> ")
        if choice_puzzle =="692":
            print("    ")
            print("You enter the code and take the lock off the tackle box.")
            time.sleep(2)
            print("You open it to find a picture of Alice next to a column under the dock.")
            time.sleep(2)
            print("You cautiosly make your way down to the beam in order to find hints.")
            time.sleep(2)
            print("You notice the post has a message on it. It reads:")
            time.sleep(2)
            print("  ")
            print("[Post, Line, Word]")
            print("   ")
            time.sleep(2)
            # docks_complete=True
            check()
        else:
            print("   ")
            print("This code is incorrect. Hint: It's in a picture on the blog.")

#**********Docks puzzle 1**********

def dock_puzzle_1():
    print(" ")
    print("It reads:")
    time.sleep(2)
    print('''   "Feed me and I live,
    Give me a drink and I die.
    What am I?"''')
    print(" ")
    time.sleep(2)
    print("The riddle seemingly hinted to the location of the key - how the kidnapper knew where it was -")
    time.sleep(2)
    print("you did not know.")
    time.sleep(2)
    print(" ")
    choice_puzzle="" #Place Holder
    choice_puzzle_2="" #Place Holder
    x=True #Place Holder
    
    while x==True:
        while choice_puzzle != "fire":
            print("What is it?")
            print("-----------------------------")
            choice_puzzle = input(">> ")
            if choice_puzzle == "fire":
                print(" ")
                print("You figure out the answer is fire, so you look around for anything that points to fire.")
                time.sleep(2)
                print("After thinking of all the locations, you recall there is a fire pit somewhere in the vicinity.")
                time.sleep(2)
                print(" ")
                while choice_puzzle_2 != "cabin":
                    choice_puzzle_2 = input("Where is the fire pit?")
                    if choice_puzzle_2 == "cabin":
                        print(" ")
                        print("You go to the fire pit. The embers were fresh, a fire was recently lit here the night before.")
                        time.sleep(2)
                        print("Glancing into the pit, you see something shine and dig out the copied key.")
                        time.sleep(2)
                        print("You open the gate and leave the key in place of the note.")
                        time.sleep(2)
                        x=False
                        dock_puzzle_2()
                    else:
                        print("")
                        print("Nope that isn't it")
                        time.sleep(2)
            else:
                print("")
                print("Invalid Input")
                time.sleep(2)


#**********Docks**********

def docks():
    print("You go to the dock to admire the cool air, fresh water smell, and the sound of the moving water.")
    time.sleep(2)
    print("But instead, you end up stuck at the front of the gate to the lake, just about 100 meters")
    time.sleep(2)
    print("away from the dock. You look for the copied key that you and Alice made, that is typically")
    time.sleep(2)
    print("hidden in a pot under a tree near the gate, but instead you find a note in place of the key.")
    time.sleep(2)
    global docks_complete
    docks_complete = True
    dock_puzzle_1()
    
    
#**********Friend's House Puzzle 2**********

def friend_house_puzzle_2(): #puzzle 2 for friend's house
    choice_puzzle= False #Place Holder
    print("You pick up the phone and inspect it.")
    time.sleep(2)
    print("With your string of technological luck, it is locked, and none of the old passwords you know work.")
    time.sleep(2)
    print("A little note is on the back of the phone")
    print(" ")
    time.sleep(2)
    print("It reads:")
    time.sleep(2)
    print ('''All things have a time stamp. The answer to this is the first timestamp.''')
    print("  ")
    time.sleep(2)
    print ("So far you've gotten the hange of this, and guess what you look at?")
    time.sleep(2)
    print ("That's right, the BLOG!!!")
    time.sleep(2)
    print("  ")
    while choice_puzzle !=  "3911":
            print("What is the code?")
            print("*it's a four-digit number")
            print("-----------------------------")
            choice_puzzle = input(">> ")
            if  choice_puzzle =="3911":
                print(" ")
                print("You successfully open the phone and you believe you have it all under control.")
                time.sleep(2)
                print("However, you lose the sense of security very quickly.")
                time.sleep(2)
                print("A soon as you touch the screen the phone takes off without you.")
                print(" ")
                time.sleep(2)
                print("You attempt to regain control, but the phone doesn't respond.")
                print(" ")
                time.sleep(2)
                print("In the blink of an eye the phone opens the browser app and opens the blog.")
                time.sleep(2)
                print("It pulls up blog post #3, and stays stuck there.")
                time.sleep(2)
                print("You note down the post and notice a striking similarity to the email.")
                time.sleep(2)
                # friend_house_complete ==True
                check()
            else:
                print("")
                print("Invalid Input")
                time.sleep(2)
                friend_house_puzzle_2()
                
#**********Friend's House Puzzle 1**********

def friend_house_puzzle_1(): #puzzle 1 for friend's house
    choice_puzzle = False #Place Holder
    print(" ")
    print("You look around the familiar, grandiose room. You see the bed to your right, a closet just behind it,")
    time.sleep(2)
    print("a desk to your left with papers all over it, a bookshelf lined with colorful books -")
    time.sleep(2)
    print("most of them untouched. Because of all the contact you've made with her through technology, you think")
    time.sleep(2)
    print("about any technology that could have been left behind. She used her phone very often...")
    print(" ")
    time.sleep(2)
    print("You ask the police about it, and they tell you that they had tracked it to the house, but could not identify it's exact location.")
    time.sleep(2)
    print("You glance at the blog for any clues as to where the phone could be.")
    time.sleep(2)
    print(" ")
     
    while choice_puzzle != "closet":
        choice_puzzle = input("Where is the phone?")
        if choice_puzzle == "closet":
            print(" ")
            print("You walk into the expansive closet. One wall is covered in shoes, the other three are")
            time.sleep(2)
            print("covered in clothes and a mirror is located at every corner. There is a lounging chair in the middle")
            time.sleep(2)
            print("of the room. Resting neatly on the chair, parallel and propped up as if it was waiting for you, was the phone.")
            time.sleep(2)
            print("A chill runs down your spine, it was too easy to find, especially if the police had already looked for it.")
            time.sleep(2)
            print(" ")
            friend_house_puzzle_2()
        elif choice_puzzle == "bed":
            print(" ")
            print("The bed is filled with plush cushions and blankets, a place you'd except Alice to lay and text.")
            time.sleep(2)
            print("Rumaging through the covers, your search is in vain as you come up with nothing of importance.")
            time.sleep(2)
            print(" ")
        elif choice_puzzle == "desk":
            print(" ")
            print("You move over to the messy desk, and shift the papers aside. Nothing of value is on top of the desk,")
            time.sleep(2)
            print("so you decide to check the drawers. More random items, and no phone; you turn back and look elsewhere.")
            time.sleep(2)
            print(" ")
        elif choice_puzzle == "bookshelf":
            print(" ")
            print("Walking over towards the aged bookshelf, you give a quick look on the top to see if you can find the phone.")
            time.sleep(2)
            print("More decorations and faux plants, but still no phone. Checking behind the books, you noticed that they haven't been moved")
            time.sleep(2)
            print("in a while. Although you find some of her old homework stashed away, the phone is still missing.")
            time.sleep(2)
            print(" ")
        else:
            print("")
            print("Invalid Input")
            time.sleep(2)
            friend_house_puzzle_1()


#**********Friend's House**********

def friend_house():
    print("You enter the house and are greeted by your friend's parents.")
    time.sleep(2)
    print("All three of you exchange hugs, and Alice's mother clings onto her husband for support.")
    time.sleep(2)
    print('"I am so glad you are okay, I just hope Alice is too."')
    time.sleep(2)
    print("She began to cry, largely failing to hold back her tears.")
    print(" ")
    time.sleep(2)
    print("Typically you'd expect the mother of a fairly rich girl to be all weepy, ")
    print("but Alice's mother was a very reliable and strong person - ")
    print("you'd seen her get through so much - ")
    print("but loosing her child seemed to rip at her.")
    print(" ")
    time.sleep(2)
    print("Alice's father leans against her to hold her up.")
    time.sleep(2)
    print("You ask for permission to see Alice's room.")
    time.sleep(2)
    print("You told them that you wanted to find a lead if you could.")
    time.sleep(2)
    print("They protest for your sake,")
    print("but your stubborn, mule like presistence gains you access to her room.")
    print(" ")
    time.sleep(2)
    global friend_house_complete
    friend_house_complete = True
    
    x=True #Place Holder
    while x==True:
        print("")
        print("What do you do?")
        print("-----------------------------")
        print("[1]Go to her room")
        print("[2]Leave location")
        selected=input(">> ")
        if selected=="1":
            x=False
            print("You go to Alice's room")
            time.sleep(2)
            friend_house_puzzle_1()
        elif selected=="2":
            x=False
            print("You leave the house")
            time.sleep(2)
            map()
        else:
            print("")
            print("Invalid Input")
            time.sleep(2)
            #Optional, can just go to the top of the while loop without it

            friend_house()

#**********Map**********

def map(): #Hub for locations
    global friend_house_complete
    global docks_complete
    global playground_complete
    global school_complete
    print("")
    print("Where will you go?")
    print("-----------------------------")
    print("[1]Friend's House (Easy Difficulty)")
    print("[2]Docks (Hard Difficulty)")
    print("[3]School (Easy Difficulty)")
    print("[4]Playground (Medium Difficulty)")
    print("[5]Quit")
    selected=input(">> ")
    
    if selected=="1":
        if friend_house_complete==True:
            print("You've already been through here, and don't feel the need to go back.")
            time.sleep(2)
            map()
        else:    
            print("You walk to your Friend's House")
            time.sleep(2)
            friend_house()
    elif selected=="2":
        if docks_complete==True:
            print("You've already been through here, and don't feel the need to go back.")
            time.sleep(2)
            map()
        else:    
            print("You walk to the Docks")
            time.sleep(2)
            docks()
    elif selected=="3":
        if school_complete==True:
            print("You've already been through here, and don't feel the need to go back.")
            time.sleep(2)
            map()
        else:
            print("You walk to the School")
            time.sleep(2)
            school()            
    elif selected=="4":
        if playground_complete==True:
            print("You've already been through here, and don't feel the need to go back.")
            time.sleep(2)
            map()
        else:
            print("You walk to the Playground")
            time.sleep(2)
            playground()
            
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

#**********Start Area**********

def start_area(): #Tutorial!
    print("It's a bright and sunny morning, the birds are chirping like the amazing alarm clock they are and the flaming ball of")
    print("gas in the sky shines on your face through the cracks of the blinds.")
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
        
    else:
        print("Invalid Input")
        print("")
        time.sleep(2)
        start_area()            
    
    time.sleep(2)
    fixed_entry=selected.lower() #This puts the enter in all lowercase characters
    password="captain"
    remaining_guess =10
    print("")
    print("Growing ever irritated with you the computer displays a hint")
    print("Hint: Alice's Dog")
    print("She probably has a picture on her blog...")
    print("Enter a password")
    print("-----------------------------")
    
    while selected != "captain":
        selected=input(">> ")
        selected.lower() #This puts the enter in all lowercase characters
        if (selected == "captain"):
            print("Your password is accepted")
            time.sleep(2)
            print("The Desktop opens")
            time.sleep(2)
            print("")
            print("TUTORIAL COMPLETE!")
            print("")
        else:
            print("You're denied access, the password doesn not work.")
            print("Try again.")
        
            
    print("As your Desktop loads in you begin to pack for college and notice your computer notifications going off.")
    time.sleep(2)
    print("You've set for your computer to check your inbox every 24 hours.")
    time.sleep(2)
    print("However, this time the inbox went off early in the morning, rather than later in the evening like it was supposed to.")
    time.sleep(2)
    print ("You seem to be a little confused.")
    time.sleep(2)
    print("What do you do?")
    print("-----------------------------")
    print("[1]Check the computer")
    print("[2]Go back to bed")
    selected=input(">> ")     
    
    if selected=="1":
        print("You open the computer to see that your inbox was piling up with emails.")
        print("The notification shows that you have about 300 new messages.")
        time.sleep(2)
        print("The emails seem to all be spams from professors and random marketing and coupon companies you subscribed to.")
        time.sleep(2)
        print("Intermixed with these next-to-useless spam mails are a few with single letter subjects.")
        time.sleep(2)
        print("You filter these out and get the figures: h m e 5 s e s a t g ")
        time.sleep(2)
        print("If you unscramble the numbers and letters you get two words...")
        time.sleep(2)
        
        start_num=4 #Place Holder
        answer="5th message"
        while (start_num>0):
            print("What does it say? (Hint: It's a rank number and a word)")
            print("-----------------------------")            
            selected=input(">> ")
            fixed_entry=selected.lower() #This puts whatever the user entered (with the exception of numbers) into lowercase
            
            if (start_num<=2): #Prints a hint once the user has less than two chances remaining
                print("Hint: A number ranking and word")
                
            if (fixed_entry==answer): #Checks the lowercase entry against the answer variable
                start_num=0
                print(" ")
                print("You heed the note and look at the 5th message in your inbox.")
                print("It was from a no name publishing company, but as you read you realize that's not the case.")
                print("The message reads:")
                print(" ")
                time.sleep(2)
                print("3/1/2/9/14") 
                print("[12, 2, 2]")
                print("-")
                print("3Th12")
                print("  ")
                
                print("You will need this in a while - use this and the blog to find us.") #PUT THE BLOG LINK HERE
                print(" ")
                time.sleep(2)
                print("It doesn't make any sense but something about it worries you.")
                time.sleep(2)
                print("You mark the message as important and continue to browse your inbox.")
            else:
                print("Nope. That isn't right...")
                start_num=start_num-1
        
        time.sleep(2)
        print(" ")
        print("Soon you notice an email from your boss.")
        time.sleep(2)
        print("The message reads: ")
        print("  ")
        print("I realize this is your time off, however I've found something in your town.") #Spunky try hard boss is spunky
        print("A police reported a girl, I think her name is Alice, has gone missing.")
        print("If you have the time, I'd like you to cover it for us. Do you have any connections? Could you do it?")
        print("  ")
        time.sleep(2)
        print("Of course, rather than covering the story, you became a part of it. Alice was your best friend.")
        time.sleep(2)
        print("Nerves getting the best of you, you try her phone, but the call drops.")
        time.sleep(2)
        print("You call her mother to confirm it's a prank, but her mother crying on the porch tells you it's true.")
        time.sleep(2)
        print("Your one and only close friend has gone missing, and the worried you needs to find her.")
        map()
        
    elif selected=="2":
        print("You go to bed...")
        time.sleep(2)
        start_area()
    
    else:
        print("Invalid Input")
        print("")
        time.sleep(2)
        start_area()        
        
#**********Start Menu**********

def start_menu(): #First thing you see
    print("-----------------------------")
    print("Do You Get It?")
    print("-----------------------------")
    print("[1]Play")
    print("[2]Website Link")
    print("[3]Quit")
    print("")
    print("Please note that just about every puzzle will have an answer ON THE BLOG. You need the blog to get through the game.")
    print("Be carefully observant, the blog is your best friend.")
    print("The game will not take capitals, please write in lowercase. If options are available, enter the number of the option, not the option.")
    print("(Brackets not required)")
    print("")
    selected=input(">> ")
    
    #***************LOAD STUFF***************
    
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
        
    #**********Cheat Entries**********
    
    elif selected=="map":
        map()
    
    elif selected=="friendshouse":
        friend_house()
    elif selected=="friendshousepuzzle1":
        friend_house_puzzle_1()
    elif selected=="friendshousepuzzle2":
        friend_house_puzzle_2()
        
    elif selected=="docks":
        docks()
    elif selected=="dockspuzzle1":
        docks_puzzle_1()
    elif selected=="dockspuzzle2":
        docks_puzzle_2()
        
    elif selected=="school":
        school()
    elif selected=="schoolpuzzle1":
        school_puzzle_1()
    elif selected=="schoolpuzzle2":
        school_puzzle_2()
        
    elif selected=="playground":
        playground()
    elif selected=="playgroundpuzzle1":
        playground_puzzle_1()
    elif selected=="playgroundpuzzle2":
        playground_puzzle_2()
        
    elif selected =="end area":
        end_area()
    elif selected == "apple":
        selected.lower()
        print('''      Creeping was really more like very obviously walking over to you and Alice, though your mind percieved it otherwise. 
        Assuming that the female figure was the kidnapper, you pull Alice onto her feet and attempt to make a run, but Alice holds you back.
        You fear she has a version of Stockholm Syndrome for a good while, until she speaks up in her constantly cheerful voice.
        
        "You remember Blithe, right?"
        
        A flood of memories rushed in. You recall the small little girl, who somehow was more tech savvy that even the IT crews at school.
        It was abnormal for her age, somehow alot of people had trouble comprehending the fact that she knew how technology worked.
        At the age of 16, she had disappeared out of town.
        You and Alice thought she probably went to a bigger city, but according to the information Alice was giving you, she had taken on a job.
        
        Blithe had been playing Robin Hood for a while now. 
        Alice's parents funded the town, so she had little to no work to do there.
        She spent her time getting hired to hack into accounts that had ripped of customers - very legally for that matter,
        but it turns out that at some point she had actually hacked into the wrong server.
        Instead of hacking into the bank server of an illegal rip-off company, she hacked into the server of a mercenary agency.
        
        Apperently the information was top secret, and Blithe had been on the run from the mercenaries.
        
        Alice had apparently been a kidnapping target on the server when Blithe saw it, and she had decided to help keep Alice safe until everything was okay.
        They decided they needed your help to make it look like Alice had already been kidnapped and brought back by realeasing an article on your online journal.
        Looks like your boss was getting the story she wanted.
        
        You didn't know whether to applaud Alice and Blithe for pulling this off without getting caught or whether to yell at them for freaking everyone out.
        You decide to do the former, her mother would take care of the yelling.
        But as soon as you get back, Alice's mother hugs Alice, and informs you that she knew all along, and that Blithe was more than welcome to use the cabin until 
        she was safe.
        She also explained that this was why they didn't want you to go into the room in the first place - they did not want to send you on a wild goose chase.
        At this point, you simply walk off the porch after saying good bye, and are more than ready to slam something into the wall, perhaps your head.
        
        All said and done - everything ended well. Except for the fact that you've now lost a good majority of your sleep.''')
        
    else:
        print("Invalid Input")
        print("")
        time.sleep(2)
        start_menu()
            
start_menu()

