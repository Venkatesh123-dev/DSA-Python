#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 13:01:18 2020
Implementing a stack using list
@author: venky
"""
push/pop of element = o(1)
search element by value  = o(n)

stack = []

def push():
    if len(stack) == n:
        print("stack is full !!")
    else:
        element = input("please entetr a element!:")
        stack.append(element)
        print(stack)
    
    
def pop():
    if not stack:
        print("stack is empty!")
    else:
        e = stack.pop()
        print("removed element:", e)
        print(stack)
        
n = int(input("limit of statck!!!:"))        
while True:
    print("select the following option \n 1. push \n 2. pop \n 3. quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Please choose correct input")        
    
