#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 13:50:23 2023

@author: fayza
"""
balance=1500
input(("welcome to our bank \nEnter your 4-digit pin number : "))


while True:
    
    
    request=int(input("1 - Withdrow \n2 - Balance Inquiry\n3 - Fast Cash \n4 - Quit\n\nchoose process : "))

#match request :
#case 1:
    if request==1 :
        cash=int(input("Enter the required amount (multiple of 100)"))
        if not cash % 100 and cash > 0:
            if cash > balance:
                print("invalid process")
    
                
            else :
                balance=balance-cash
                print("TRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                print("take your money")
                print("your current balance = ",balance)
        else :
            print("invalid process")


    elif request==2:
        print("your balance = ",balance)
        break
    
    elif request==3:
        
        cash=int(input("choose one choice \n1- 500$\n2- 1000$\n3- 5000\n4- 10000\n5- 50000\n"))
        if ( cash==500 or cash==1000 or cash==5000 or cash==10000 or cash==50000 ) and cash >= 0:
            if cash > balance:
                print("invalid process")
    
                
            else :
                balance=balance-cash
                print("TRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR")
                print("take your money")
                print(" = ",balance)
        else :
            print("invalid process")

        
        
        
        '''money=int(input("enter your cash : "))
        if not money %100 and money>0 :
            balance=balance+money
            print("your current balance = ",balance)
        else :
            print("invalid operation")'''
            
    
    elif request==4:
        print("thank you for choosing us")
        break
    
    
    
    