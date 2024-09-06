import random
l = ["rock","paper","scissor"]

'''
rock vs paper -> win paper
rock vs scissor -> win rock
paper vs scissor -> win scissor
'''

while True:
    ccount = 0
    ucount = 0
    name = input("Enter Your Name : ")
    uc = int(input('''
Game start.....
1 : Yes
2 : No | Exit
                   '''))
    
    if uc==1:
        for a in range(1,6):
            userInput = int(input('''
1 -> Rock
2 -> Scissor
3 -> Paper
                                      '''))
            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="scissor"
            elif userInput==3:
                uchoice="paper"
            Cchoice = random.choice(l)
            if Cchoice==uchoice:
                print('computer value: ',Cchoice)
                print('User value: ',uchoice)
                print('\nRound Draw.....')
                ucount=ucount+1
                ccount=ccount+1
            elif(uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
                print('computer value: ',Cchoice)
                print('User value: ',uchoice)
                print('\nYou Win....')
                ucount=ucount+1
            else:
                print('computer value: ',Cchoice)
                print('User value: ',uchoice)
                print("\nComputer Win....")
                ccount=ccount+1
                
        if ucount == ccount:
            print("\nComputer Score : ",ccount)
            print(name, "your Score : ",ucount)
            print("\nFinal Game is Draw.....")
            break
        elif ucount > ccount:
            print("\nComputer Score : ",ccount)
            print(name, "your Score : ",ucount)
            print('\nFinally ', name, " You are Winner....")
            break
        else:
            print("\nComputer Score : ",ccount)
            print(name, "your Score : ",ucount)
            print("\nComputer is Winner.....")
            break

    else:
        break