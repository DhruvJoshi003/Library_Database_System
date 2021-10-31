'''
HEADER:

File name: Library_Database.py
Author: Dhruv Kamalkumar Joshi
Date Created: 17/10/2020
Date Completed: 04/01/2021
Python Version: 3.9
'''
import mysql.connector as m
import book as b
import member as me

def MENU():
    print('')
    print('Enter 1 to access Books Data')
    print('Enter 2 to access Members Data')
    print('Enter 3 to Exit')
    print('')

def MENUii():
    print('')
    print('Enter 1 to insert records')
    print('Enter 2 to update data')
    print('Enter 3 to search record')
    print('Enter 4 to display the table')
    print('Enter 5 to delete records')
    print('Enter 6 to go to main menu')
    print('')

def MENUi():
    print('')
    print('Enter 1 to insert records')
    print('Enter 2 to update data')
    print('Enter 3 to search record')
    print('Enter 4 to show all the available books')
    print('Enter 5 to display the table')
    print('Enter 6 to delete records')
    print('Enter 7 to go to main menu')
    print('')

print('')
print('∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇')
print('∆                                                 ∆')
print('∇        WELCOME TO FICTION\'S CORNER LIBRARY      ∇')
print('∆                                                 ∆')
print('∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇∆∇')
print('')

while True:
    MENU()
    choice1=str(input('So, what will it be? : '))
    print('')

    if int(choice1)==1:
        while True:     

            MENUi()        
            choice11=str(input('So, what will it be? : '))
            print('')

            if int(choice11)==1:
                b.INS()

            elif int(choice11)==2:
                b.UPD()

            elif int(choice11)==3:
                print('')
                print('Enter 1 to search record using Book Id')
                print('Enter 2 to search record using Book Name')
                print('Enter 3 to go to the previous Menu')
                print('')

                choice113=str(input('So, what will it be? : '))
                print('')

                if int(choice113)==1:
                    b.SEA()
                elif int(choice113)==2:
                    b.SEA_N()
                elif int(choice113)==3:
                     break

                else:
                    print('\t|An error occurred due to wrong input,please try again|')
                    continue
                
            elif int(choice11)==4:
                b.SA()
                
            elif int(choice11)==5:
                b.DIS()

            elif int(choice11)==6:
                b.DEL()

            elif int(choice11)==7:
                break

            else:
                print('\t|An error occurred due to wrong input,please try again|')
                continue
        
    elif int(choice1)==2:
        while True:
            MENUii()
            choice12=str(input('So, what will it be? : '))
            print('')

            if int(choice12)==1:
                me.INS()

            elif int(choice12)==2:
                me.UPD()

            elif int(choice12)==3:
                print('')
                print('Enter 1 to search record using Member Id')
                print('Enter 2 to search record using Member Name')
                print('')

                choice123=str(input('So, what will it be? : '))
                print('')

                if int(choice123)==1:
                    me.SEA()
                    
                elif int(choice123)==2:
                    me.SEA_N()

                elif int(choice123)==3:
                    break

                else:
                    print('\t|An error occurred due to wrong input,please try again|')
                    continue               

            elif int(choice12)==4:
                me.DIS()

            elif int(choice12)==5:
                me.DEL()

            elif int(choice12)==6:
                break

            else:
                print('\t|An error occurred due to wrong input,please try again|')
                continue

    elif int(choice1)==3:
        print('')
        print('\t| Cya again somtime :) |\n')
        break

    else:
        print('\t|An error occurred due to wrong input,please try again|')
        continue 







