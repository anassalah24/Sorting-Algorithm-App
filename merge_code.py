from os import read, startfile, times
from tkinter import Label
from RandomGenerator import randomgenerator
import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import math



""" merge sort function """

def merge_sort(array, left_index, right_index,count):
    
    if left_index >= right_index:
        return count
    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle,count)
    merge_sort(array, middle + 1, right_index,count)
    c=merge(array, left_index, right_index, middle)
    count=count+c
    
    return count



""" Merge code function """
""" In merge code i dont use sentinels """

def merge(array, left_index, right_index, middle): 
    
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]
    
    countM=len(left_copy)+len(right_copy)
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index


    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
            
            
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1
            
            

        countM=countM+2
        sorted_index = sorted_index + 1

   
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1
        countM=countM+3
        

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1
        countM=countM+3
        
         
    return countM    
          



def main_merge(a):
    

     times=[0]*99
     arr_n=[0]*99
     time_notation=[0]*99 
     i=0

     for n in range(10,1000,10):
        rand_array=[0]*n
        randomgenerator(rand_array,n)

        count=0

        count=merge_sort(rand_array,0,len(rand_array)-1,count)

        
        times[i]=count
        i+=1
     
     """ filling arr_n """
     z=0     
     for i in range(10,1000,10):
        arr_n[z]=i
        z+=1
     '''  filling time_notation      '''
     if(a==0):
        w=0
        for w in range(len(arr_n)):
            time_notation[w]=(arr_n[w]*math.log2(arr_n[w]))/2
            
         
           
     print("For Each Array Generated with different N sorted using Merge Sort, Steps were:")
     print(times)
    
 
     # Dataset
     x = np.array(arr_n)
     y = np.array(times)
     if(a==0): 
        x1 = np.array(arr_n)
        y1 = np.array(time_notation)
        X_Y_Spline1 = make_interp_spline(x1, y1)
        x_1 = np.linspace(x1.min(), x1.max(), 500)
        y_1 = X_Y_Spline1(x_1)
        plt.plot(x_1,y_1,label="NLOG(N)")
        plt.title("Merge Sort")
        plt.legend()
    
     
     X_Y_Spline = make_interp_spline(x, y)
 
     # Returns evenly spaced numbers
     # over a specified interval.
     X_ = np.linspace(x.min(), x.max(), 500)
     Y_ = X_Y_Spline(X_)
     plt.plot(X_, Y_,label ='Merge Sort')
     plt.xlabel("N")
     plt.ylabel("Steps")
     


