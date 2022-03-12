from os import read, startfile
from RandomGenerator import randomgenerator
import time
import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import math


def partition(arr, low, high,count):
       i = (low-1)
       pivot = arr[high]
       
       for j in range(low, high):
              if arr[j] <= pivot:
                     i = i+1
                     arr[i], arr[j] = arr[j], arr[i]
                     count=count+3
              count=count+1
			
       arr[i+1], arr[high] = arr[high], arr[i+1]
       return (i+1),count;	
	
 

def quickSort(arr, low, high,count):
       if len(arr) == 1:
              return count
           
       if low < high:
              pi,count = partition(arr, low, high,count)
              quickSort(arr, low, pi-1,count)
              quickSort(arr, pi+1, high,count)       
       return count
		
 

def main_quick(a):
    

     times=[0]*99
     arr_n=[0]*99
     time_notation=[0]*99
     i=0

     for n in range(10,1000,10):
        rand_array=[0]*n
        randomgenerator(rand_array,n)

        count=0

        count=quickSort(rand_array,0,len(rand_array)-1,count)

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
            time_notation[w]=(arr_n[w]*math.log(arr_n[w],2))/2.5 
         
     
          
     print("For Each Array Generated with different N sorted using Quick Sort, Steps were:")
     print(times)   
 
     # Dataset
     x = np.array(arr_n)
     y = np.array(times)
     if(a==0): 
       x1 = np.array(arr_n)
       y1 = np.array(time_notation)
       X_Y_Spline1 = make_interp_spline(x1, y1)
       x_1 = np.linspace(x1.min(), x1.max(),500)
       y_1 = X_Y_Spline1(x_1)
       plt.plot(x_1,y_1,label="NLOG(N)")
       plt.title("Quick Sort")
       plt.legend()
     
     X_Y_Spline = make_interp_spline(x, y)
 
     # Returns evenly spaced numbers
     # over a specified interval.
     X_ = np.linspace(x.min(), x.max(), 500)
     Y_ = X_Y_Spline(X_)
     # Plotting the Graph
     plt.plot(X_, Y_,label ='Quick Sort')
     plt.xlabel("N")
     plt.ylabel("Steps")
     






