              #PROJECT-1 Snake,Water,Gun Game 

import random

'''
1 for snake
-1 for water
0 for gun
'''
 
computer = random.choice([-1,0,1])
youstr = input("Enter your choice :")
youDict = {"s": 1 , "w": -1 ,"g":0}
reverseDict = { 1 : 'Snake', -1 : "Water" , 0 : "Gun"}

you = youDict[youstr]

#By now we have 2 numbers (variables), you and computer

print(f"You Chose {reverseDict[you]}\nComputer Chose {reverseDict[computer]}")

if (computer == you):
    print("Its a tie ")

else :
    if (computer== 1 and you == -1 ):
        print("You Lose!")
    elif (computer== 1 and you == 0 ):
        print("You Win!")
    elif (computer== -1 and you == 1 ):
        print("You win!")
    elif (computer== -1 and you == 0 ):
        print("You Lose!")
    elif (computer== 0 and you == -1 ):
        print("You win!")
    elif (computer== 0 and you == 1 ):
        print("You Lose!")
    else :
        print("Something Went Wrong")



#______________________shortened way ________________________

if (computer == you):
    print("Its a tie ")


else :
    '''
    if (computer== 1 and you == -1 ):  (computer - you) = 2
        print("You Lose!")
    elif (computer== 1 and you == 0 ): (computer - you ) = 1
        print("You Win!")
    elif (computer== -1 and you == 1 ): (computer - you ) = -2
        print("You win!")
    elif (computer== -1 and you == 0 ):  (computer - you ) = -1
        print("You Lose!")
    elif (computer== 0 and you == -1 ):  (computer - you ) = 1
        print("You win!")
    elif (computer== 0 and you == 1 ):  (computer - you ) = -1
        print("You Lose!")
    else :
        print("Something Went Wrong")
    '''
   # the below logic is written on the basis of the value of [computer - you] ,
   # [by observing pattern  and to reduce code length ]
    

if((computer - you) == -1 or (computer - you == 2)):
    print('You Lose')
else :
    print("You win")
