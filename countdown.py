# -*- coding: utf-8 -*-
"""
Created on Sat May  2 00:37:44 2026

@author: MOHAMMAD FARAZ
"""

n = int(input("Enter the number:"))
def countdown(n):
    
    if  n <= 10:
        print("Blastoff")
    else: 
        print(n)
        countdown(n-1)         
        print(n)
        
countdown(n)