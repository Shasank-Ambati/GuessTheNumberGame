import random

def CheckingTheGuess(usernum,num):
    if num<usernum:
        print('You need to guess Lower')
        usernum=int(input('Guess the Number:'))
        CheckingTheGuess(usernum,num)
    elif num>usernum:
        print('You need to guess Higher')
        usernum=int(input('Guess the Number:'))
        CheckingTheGuess(usernum,num)
    else:
        print('your guess was right!!!! congratulations!!!')
        TryAgain=input('Do you want to try again?(y/n):')
        if TryAgain=='y':
            num=random.randint(1,100)
            usernum=int(input('Guess the Number:'))
            CheckingTheGuess(usernum,num)
        else:
            print('Thank you for playing')

num=random.randint(1,100)
usernum=int(input('Guess the Number:'))
CheckingTheGuess(usernum,num)

