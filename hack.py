# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 13:23:37 2020 
Difficulty Level: Easy
@author: iCule10
"""
def maxi(arr):

     arr_size = len(arr)
    
     max_diff = arr[1] - arr[0]
     for i in range( 0, arr_size ): 
         for j in range( i+1, arr_size ): 
             if(arr[j] - arr[i] > max_diff):  
                 max_diff = arr[j] - arr[i]
    
     print(max_diff)
    
maxi([7,1,2,5])