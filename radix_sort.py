from os import read, startfile
from RandomGenerator import randomgenerator
import time
import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt



def countingSort(arr, exp1,count1):
	
      n = len(arr)
      output = [0] * (n)
      count = [0] * (10)
      
      for i in range(0, n):
        index = (arr[i]/exp1)
        count[int((index)%10)] += 1

      for i in range(1,10):
        count[i] += count[i-1]
      

      i = n-1
      while i>=0:
        index = (arr[i]/exp1)
        output[ count[ int((index)%10) ] - 1] = arr[i]
        count[int((index)%10)] -= 1
        i -= 1
      
      
      i = 0
      for i in range(0,len(arr)):
        arr[i] = output[i]
      return count1

def radixSort(arr,count1):
      max1 = max(arr)
      exp = 1
      
      while (max1/exp) > 0:
            countingSort(arr,exp,count1)
            exp *= 10
         
      count1=count1+(2*len(arr))+9       
      return count1*2
    		
	
	
  
	


def main_radix(a):
     times=[0]*10
     arr_n=[0]*10
     time_notation=[0]*10 
     i=0

     for n in range(10,1000,100):
        rand_array=[0]*n
        randomgenerator(rand_array,n)

        
        count1=0
        count1=radixSort(rand_array,count1)


        times[i]=count1
        i+=1
    
     """ filling arr_n """
     z=0     
     for i in range(10,1000,100):
        arr_n[z]=i
        z+=1
     '''filling time_notation'''
     if(a==0):
       w=0
       for w in range(len(arr_n)):
         time_notation[w]=2*(arr_n[w]+99)*2
           
    
     print("For Each Array Generated with different N sorted using Radix Sort, Steps were:")
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
       plt.plot(x_1,y_1,label="d*(N+K)")
       plt.title("Radix Sort")
       plt.legend()
      
     X_Y_Spline = make_interp_spline(x, y)
 
     # Returns evenly spaced numbers
     # over a specified interval.
     X_ = np.linspace(x.min(), x.max(), 500)
     Y_ = X_Y_Spline(X_)
     # Plotting the Graph
     plt.plot(X_, Y_,label ='Radix Sort')
     plt.xlabel("N")
     plt.ylabel("Steps")
     


