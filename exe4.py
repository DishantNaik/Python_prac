# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 01:42:50 2020

@author: iCule10
"""
def run(n):
    ans = [1]
    for i in range(2,n):
        if n % i == 0:
            ans.append(i)
    return ans
    
if __name__=='__main__':
    print("Enter a number: ")
    n = int(input())
    print (run(n))