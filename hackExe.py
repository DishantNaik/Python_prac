# -*- coding: utf-8 -*-
"""
Created on Sat May  9 22:52:48 2020
Provlem description:Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
                    You are given  scores. Store them in a list and find the score of the runner-up.
Difficulty Level: Easy
@author: disha
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr1 = list(arr)
    arr1.sort(reverse = True)
    
    if(arr1[0] != arr1[1]):
        print(arr1[1])
    else:
        length = len(arr1)
        for i in range(length):
            if(arr1[i] != arr1[i +1]):
                tmp = arr1[i +1]
                break
        print(tmp)