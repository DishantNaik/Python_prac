# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 01:27:48 2020

@author: iCule10
"""
def run(lis):
    ans = []
    for i in lis:
        if i < 5: ans.append(i)
    return ans
    
if __name__=='__main__':
    lis = []
    n = int(input("Enter number of elements : "))
    for i in range(0,n):
        print("Enter number " + str(i + 1) + ":")
        ele = int(input()) 
        lis.append(ele)
    print (run(lis))