# 1A2B Game: guess the number

import random

def Game1A2B():
    print("Welcome to our 1A2B Game")
    print("This is a game about guessing the numbers")
    print("There will be 4 numbers,")
    print("If you guess any number totally correct, you get an A")
    print("If you guess any number correct but wrong place, you get a B")
    print("When you get 4A, then you win the game!")

    ans = 0

    while(ans == 0):
        ans = int(random.random()*10000)
        for i in range(4):
            for j in range(4):
                if i!=j:
                    if (ans//(10**i))%10 == (ans//(10**j))%10:
                        ans = 0

    A = 0
    Cnt = 0
    while(A < 4):
        user = int(input("Please guess a number (no duplicated): "))
        A = 0
        B = 0
        for i in range(4):
            for j in range(4):
                if (ans//(10**i))%10 == (user//(10**j))%10:
                    if i == j:
                        A = A+1
                    else:
                        B = B+1
        print(A,"A",B,"B")
        Cnt = Cnt + 1
    if(A == 4):
        print("You WIn!")
        print("Your have tried", Cnt, "times")
        Reply = input("Wanna play again? (y/n)")
        if (Reply == 'y'):
            Game1A2B()
        else:
            print("Thanks for your play!")

Game1A2B()
                    
'''
if(ans%10 == user%10):
    A = A +1

if((ans//10)%10 == (user//10)%10):
    A = A +1

if((ans//100)%10 == (user//100)%10):
    A = A +1

if((ans//1000)%10 == (user//1000)%10):
    A = A +1
    
if(ans%10 == (user//10)%10) or (ans%10 == (user//100)%10) or (ans%10 == (user//1000)%10):
    B = B +1

if((ans//10)%10 == user%10) or (ans%10 == (user//100)%10) or (ans%10 == (user//1000)%10):
    B = B +1

if((ans//100)%10 == user%10) or (ans%10 == (user//10)%10) or (ans%10 == (user//1000)%10):
    B = B +1

if((ans//1000)%10 == user%10) or (ans%10 == (user//10)%10) or (ans%10 == (user//100)%10):
    B = B +1

print(A,"A",B,"B")

if(A == 4):
    print ("You Win!")
else:
    A = 0
    B = 0
    user = int(input("Guess a number (no duplicated)"))

'''
