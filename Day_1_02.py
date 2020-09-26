#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 17:28:56 2020

@author: venky

The issue with using a list as a stack is that list uses dymanic array internally and when it reaches its capacity it will reallocate a big chunk of memory somewhere else in memory area and copy all the elements. For example in below diagram if a list has a capacity of 10 and we try to insert 11th element, it will not allocate new memory in a different memory region, copy all 10 elements and then insert the 11th element. So overhead here is (1) allocate new memory plus (2) copy all existing elements in new memory area

Implement Stack class using a deque
"""
from collections import deque
stack = deque()


class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    
    
s = Stack()
s.push(9)
s.push(34)
s.push(78)
s.push(12)
print(s.push(5))
print(s.is_empty())  
print(s.peek())  