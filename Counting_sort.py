from os import read, startfile
from RandomGenerator import randomgenerator
import time
import numpy as np
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt








def countingSort(inputArray,count):
    
    maxElement= max(inputArray)

    countArrayLength = maxElement+1

    
    countArray = [0] * countArrayLength
    count=count+(2*len(inputArray))+countArrayLength-1
    
    for el in inputArray: 
        countArray[el] += 1
    
    for i in range(1, countArrayLength):
        countArray[i] += countArray[i-1] 

    
    outputArray = [0] * len(inputArray)
    i = len(inputArray) - 1
    while i >= 0:
        currentEl = inputArray[i]
        countArray[currentEl] -= 1
        newPosition = countArray[currentEl]
        outputArray[newPosition] = currentEl
        i -= 1

    return count



def main_counting(a):
     times=[0]*10
     arr_n=[0]*10
     time_notation=[0]*10 
     i=0

     for n in range(10,1000,100):
        rand_array=[0]*n
        randomgenerator(rand_array,n)
        count=0
        count=countingSort(rand_array,count)
        times[i]=count
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
            time_notation[w]=(arr_n[w]+99)*2
           
    
    
     print("For Each Array Generated with different N sorted using Counting Sort, Steps were:")
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
        plt.plot(x_1,y_1,label="N+K")
        plt.title("Counting Sort")
        plt.legend()
     
     X_Y_Spline = make_interp_spline(x, y)
 
     # Returns evenly spaced numbers
     # over a specified interval.
     X_ = np.linspace(x.min(), x.max(), 500)
     Y_ = X_Y_Spline(X_)
     # Plotting the Graph
     plt.plot(X_, Y_,label ='Counting Sort')
     plt.xlabel("N")
     plt.ylabel("Steps")
     
    
    
    
  