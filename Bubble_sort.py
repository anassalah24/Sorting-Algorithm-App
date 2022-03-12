from os import read, startfile
from RandomGenerator import randomgenerator
import time
import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt


def bubbleSort(arr,count):
      
      n = len(arr)
      count=count+1
      for i in range(n-1):
            count=count+1
            for j in range(0, n-i-1):
                  count=count+1
                  if arr[j] > arr[j + 1] :
                        count=count+1
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
      return count                  
                
            
def main_bubble(a):
    

     times=[0]*99
     arr_n=[0]*99
     time_notation=[0]*99 
     i=0

     for n in range(10,1000,10):
        rand_array=[0]*n
        randomgenerator(rand_array,n)

        count=0

        count=bubbleSort(rand_array,count)

        
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
         time_notation[w]=pow(arr_n[w],2)
           
    
       
    
     print("For Each Array Generated with different N sorted using Bubble Sort, Steps were:")
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
       plt.plot(x_1,y_1,label="N^2")
       plt.title("Bubble Sort")
       plt.legend()
     
     X_Y_Spline = make_interp_spline(x, y)
 
     # Returns evenly spaced numbers
     # over a specified interval.
     X_ = np.linspace(x.min(), x.max(), 500)
     Y_ = X_Y_Spline(X_)
     # Plotting the Graph
     plt.plot(X_, Y_,label ='Bubble Sort')
     plt.xlabel("N")
     plt.ylabel("Steps")
    


