
import random
import time
from os import read, startfile
from RandomGenerator import randomgenerator
import time
import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import math


def MaxHeapify(arr, n, i,count):
    largest = i  
    l = 2 * i + 1
    r = 2 * i + 2 
    count=count+6
   
    if l < n and arr[i] < arr[l]:
        largest = l
  
    
    if r < n and arr[largest] < arr[r]:
        largest = r
  
   
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        MaxHeapify(arr, n, largest,count)
    return count    

def buildmaxheap(arr,n,count):
    
    for i in range((n // 2) - 1, -1, -1):
        count=MaxHeapify(arr, n, i,count)
    return count

def heapSort(arr,count):
    n = len(arr)

    count=buildmaxheap(arr,n,count)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        count=MaxHeapify(arr, i, 0,count)
    return count

def main_heap(a):
     times=[0]*99
     arr_n=[0]*99
     time_notation=[0]*99 
     i=0

     for n in range(10,1000,10):
        rand_array=[0]*n
        randomgenerator(rand_array,n)

        count=0

        count=heapSort(rand_array,count)

       

        
        times[i]=count
        i+=1
    
     """ filling arr_n """
     z=0     
     for i in range(10,1000,10):
        arr_n[z]=i
        z+=1
     '''  filling time_notation '''
     if(a==0):
         w=0
         for w in range(len(arr_n)):
            time_notation[w]=(arr_n[w]*math.log2(arr_n[w]))
         
           
    
    
     print("For Each Array Generated with different N sorted using Heap Sort, Steps were:")
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
        plt.title("Heap Sort")
        plt.legend()
     
     X_Y_Spline = make_interp_spline(x, y)
 
     # Returns evenly spaced numbers
     # over a specified interval.
     X_ = np.linspace(x.min(), x.max(), 12000)
     Y_ = X_Y_Spline(X_)
     # Plotting the Graph
     plt.plot(X_, Y_,label ='Heap Sort')
     plt.xlabel("N")
     plt.ylabel("Steps")
     
    



