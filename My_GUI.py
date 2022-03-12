from tkinter import ttk
from tkinter import *
from tkinter import font
import tkinter as tk
from typing import Sized
from InsertionSort import main_insertion
from merge_code import main_merge, merge
from HeapSort import main_heap
from SelectionSort import main_selection
from Counting_sort import main_counting
from radix_sort import main_radix
from quickSort import main_quick
from Bubble_sort import main_bubble
import matplotlib.pyplot as plt
import tkinter.font as tkFont

window=Tk()
window.title("Sorting Application")
window.iconbitmap("university.ico")
window.geometry("700x700")
window.config(bg='#2E2E2E')
fontStyle = tkFont.Font(family="Poor Richard", size=30)
fontStyle1 = tkFont.Font(family="Poor Richard", size=25)
fontbutton=tkFont.Font(family="Poor Richard", size=15)
header_frame=Frame(window).pack(padx=200)
header=Label(header_frame,text="SORTING ALGORITHM APP",bg='#2E2E2E',pady=10,fg="#1A5BF3",font=fontStyle).pack(fill=X)


""" functions """
def insertion(a):
    main_insertion(a)
    if(a==0):
        plt.show()
def Merge(a):
    main_merge(a)
    if(a==0):
        plt.show()
def Heap(a):
    main_heap(a)
    if(a==0):
        plt.show()
def selection(a):
    main_selection(a)
    if(a==0):
        plt.show()
def counting(a):
    main_counting(a)
    if(a==0):
        plt.show() 
def radixSort(a):
    main_radix(a)
    if(a==0):
        plt.show()                       
def quick(a):
    main_quick(a)
    if(a==0):
        plt.show()
def bubble(a):
    main_bubble(a)
    if(a==0):
        plt.show()
      
def openNewWindow():
    newWindow = Toplevel(window)
    newWindow.title("Project")
    newWindow.iconbitmap("university.ico")
    newWindow.geometry("750x750")
    newWindow.config(bg="#2E2E2E")
    fontStyle2 = tkFont.Font(family="Poor Richard", size=20)
    Label(newWindow,text ="CHOOSE ANY NUMBER OF ALGORITHMS TO COMPARE",fg="#1C49B4",bg='#2E2E2E',font=fontStyle2).pack()  
    def compare():
            fig = plt.figure()
            if(var1.get()==1):                    
                insertion(1)
            if(var2.get()==1):
                Merge(1)
            if(var3.get()==1):
                Heap(1)    
            if(var4.get()==1):
                selection(1)
            if(var5.get()==1):
                counting(1)
            if(var6.get()==1):
                radixSort(1)
            if(var7.get()==1):
                quick(1)
            if(var8.get()==1):
                bubble(1)
            plt.legend()                    
            plt.show()
          
        
    var1 = tk.IntVar()
    var2 = tk.IntVar()
    var3 = tk.IntVar()
    var4 = tk.IntVar()
    var5 = tk.IntVar()
    var6 = tk.IntVar()
    var7 = tk.IntVar()
    var8 = tk.IntVar()
    c1 = tk.Checkbutton(newWindow, text='Insertion Sort',variable=var1, onvalue=1, offvalue=0 ,font=fontbutton,bg="#C388E1").pack(pady=10)
    c2 = tk.Checkbutton(newWindow, text='Merge Sort',variable=var2, onvalue=1, offvalue=0,font=fontbutton,bg="#C388E1").pack(pady=10)
    
    c3 = tk.Checkbutton(newWindow, text='Heap Sort',variable=var3, onvalue=1, offvalue=0,font=fontbutton,bg="#C388E1").pack(pady=10)
    c4 = tk.Checkbutton(newWindow, text='Selection Sort',variable=var4, onvalue=1, offvalue=0,font=fontbutton,bg="#C388E1").pack(pady=10)
    
    c5 = tk.Checkbutton(newWindow, text='Counting Sort',variable=var5, onvalue=1, offvalue=0,font=fontbutton,bg="#C388E1").pack(pady=10)
    c6 = tk.Checkbutton(newWindow, text='Radix sort',variable=var6, onvalue=1, offvalue=0,font=fontbutton,bg="#C388E1").pack(pady=10)
    
    c7 = tk.Checkbutton(newWindow, text='Quick Sort',variable=var7, onvalue=1, offvalue=0,font=fontbutton,bg="#C388E1").pack(pady=10)
    c8 = tk.Checkbutton(newWindow, text='Bubble Sort',variable=var8, onvalue=1, offvalue=0,font=fontbutton,bg="#C388E1").pack(pady=10)
    
    Show_comparison=Button(newWindow,text="CLICK TO SHOW COMPARISON !!",bg="#1C49B4",font=("arial",12),pady=30,relief=RAISED,command=compare).pack(fill=X,pady=50)




""" buttons """
body=Frame(window).pack(padx=10,pady=10)
choose=Label(body,text="PLEASE CHOOSE AN ALGORITHM",font=fontStyle1,fg="#1C49B4",bg='#2E2E2E').pack()
insertion_button=Button(body,text="Insertion Sort",bg="#622D7E",font=fontbutton,pady=10,command=lambda : insertion(0),relief=RAISED).pack(fill=X)
Mergesort_button=Button(body,text="Merge Sort",bg="#79379C",font=fontbutton,pady=10,command=lambda : Merge(0),relief=RAISED).pack(fill=X)
Heapsort_button=Button(body,text="Heap Sort",bg="#8A44B0",font=fontbutton,pady=10,command=lambda : Heap(0),relief=RAISED).pack(fill=X)
selection_button=Button(body,text="Selection Sort",bg="#9B4FC3",font=fontbutton,pady=10,command=lambda : selection(0),relief=RAISED).pack(fill=X)
Counting_button=Button(body,text="Counting Sort",bg="#A75DCE",font=fontbutton,pady=10,relief=RAISED,command=lambda : counting(0)).pack(fill=X)
Radix_button=Button(body,text="Radix Sort",bg="#AE68D3",font=fontbutton,pady=10,relief=RAISED,command=lambda :radixSort(0)).pack(fill=X)
Quick_button=Button(body,text="Quick Sort",bg="#BA7ADB",font=fontbutton,pady=10,relief=RAISED,command=lambda : quick(0)).pack(fill=X)
Bubble_button=Button(body,text="Bubble Sort",bg="#C388E1",font=fontbutton,pady=10,relief=RAISED,command=lambda : bubble(0)).pack(fill=X)


next_window =Button(
    body,text="CLICK TO CHOOSE MULTIPLE ALGORITHMS TO COMPARE ",
    bg="#DBAEF2",
    fg="black",
    font=fontbutton,
    pady=10,command=openNewWindow).pack(pady=20)





window.mainloop()