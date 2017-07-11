from random import randint
#imports a random integer to be used#
question=input("Do you want to roll the dice?")#user input to start game
game=True
while game:
    if question == "yes" or question=="Yes":
        number= (randint(1,6))
    if question=='no' or question=="No":
        print("See you next time!")
        break
           
    #sets up the user input and asks if the user wants to play#
    guess=int(input("what is your guess"))
    if guess == number:
        print("you are correct the dice is:" + str(number))

        gamer=input("do you want to keep playing?")

        if gamer=="yes" or gamer=="Yes":
            continue
        if gamer=='no' or gamer=="No":
            print("See you next time!")
            game= False
    else:
        print("I'm sorry the correct answer is:" + str(number))

        gamer=input("do you want to keep playing?")

        if gamer=="yes" or gamer=="Yes":
            continue
        if gamer=="no" or gamer=="No":
            print("The correct answer was:",str(number),"better luck next time!")
            game=False

           
    
    

    
