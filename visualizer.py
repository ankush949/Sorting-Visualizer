from tkinter import *
import random

root =Tk()
root.title('Sorting Visualizer')
root.geometry('1100x700')
root.resizable(False,False)

# Instructions for sorting visualizer
def instructions():
    instruct = Toplevel()
    instruct.title('Instructions for Sorting Visualizer')
    instruct.geometry('600x320')
    instruct.resizable(False,False)

    heading = Label(instruct,text=' Instructions for Sorting Visualizer',font=("Arial", 18, "bold"),justify=LEFT)
    heading.grid(row=0,column=0,pady=(0,10))

    ins1Var = StringVar()
    ins1Var.set('This sorting algorithm visualizer is designed to help you understand how various \nsorting algorithms work behind the scenes in our systems. Each bar in the visualizer \nrepresents a number in an array, and as the algorithms run, you can see the sorting \nprocess in action. The visualizer operates based on the instructions provided \nbelow:')
    ins1 = Label(instruct,textvariable=ins1Var,font=("Arial", 12),justify=LEFT).grid(row=1,column=0,padx=(8,0))

    ins2 = Label(instruct,text='1. No button will work at the time of sorting .',font=("Arial", 12)).grid(row=2,column=0,padx=(8,0))

    ins3Var = StringVar()
    ins3Var.set('2. Colour Scheme of Bars: \na. White Bar -> Unsorted Bar \nb. Blue Bar -> Comparison or Selected \nc. Red Bar -> At Swap Time \nd. Green Bar -> Sorted')
    ins3 = Label(instruct,textvariable=ins3Var,font=("Arial", 12),justify=LEFT).grid(row=3,column=0,padx=(8,0))

    ins4 = Label(instruct,text='3. Please press reset after changing array size to implement it.',font=("Arial", 12),justify=LEFT).grid(row=4,column=0,padx=(8,0))


# Bubble Sort algorithm With bar colour mentiond
def bubbleSort():
    bubbleLabel()
    for i in range(len(data)):
        for j in range(len(data)-i-1):
            # Mark the elements blue which is going to be compare
            drawArray(data,['green' if x>=len(data)-i  else 'blue' if x==j or x==j+1 else 'white' for x in range(len(data))])
            root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
            if data[j]>data[j+1]:
                data[j],data[j+1]=data[j+1],data[j]
                #Make elments red which is swaping
                drawArray(data,['green' if x>=len(data)-i  else 'red' if x==j or x==j+1 else 'white' for x in range(len(data))])
                root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
    drawArray(data,['green' if x>=len(data)-i-1 else 'white' for x in range(len(data))])

def bubbleLabel():
    bubbleVar = StringVar()
    bubbleVar.set('Bubble Sort algorithm: \n 1. Traverse from left and compare adjacent elements and the higher one is placed at right side . \n 2. In this way, the largest element is moved to the rightmost end at first. \n 3. This process is then continued to find the second largest and place it and so on until the data is sorted . \n \n Time Complexity: O(N^2)         Space Complexity: O(1)')
    label1 = Label(root,textvariable=bubbleVar,font=("Arial", 12, "bold"),justify=LEFT,width=100).grid(row=3)

# Selection Sort algorithm With bar colour mentiond
def selectionSort():
    selectionLabel()
    for i in range(len(data)):
        minIdx=i
        for j in range(i+1,len(data)):
            drawArray(data,['green' if x<i  else 'blue' if x==j or x==j-1 or x==minIdx else 'white' for x in range(len(data))])
            root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
            if data[j]<data[minIdx]:
                minIdx=j
                drawArray(data,['green' if x<i  else 'blue' if x==j  else 'white' for x in range(len(data))])
                root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
        data[i],data[minIdx]=data[minIdx],data[i]
        drawArray(data,['green' if x<i  else 'red' if x==i or x==minIdx else 'white' for x in range(len(data))])
        root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
    drawArray(data, ['green' for _ in range(len(data))])

def selectionLabel():
    selectionVar = StringVar()
    selectionVar.set('Selection Sort algorithm: \n The algorithm iterates over the list, each time selecting the minimum element from the unsorted portion and  \n swapping it with the first element of the unsorted portion. This process is repeated for each position in the\n list until the entire list is sorted.  \n \n Time Complexity: O(N^2)         Space Complexity: O(1)')
    label1 = Label(root,textvariable=selectionVar,font=("Arial", 12, "bold"),justify=LEFT,width=100).grid(row=3)
       
# Insrtion Sort algorithm With bar colour mentiond 
def insertionSort():
    for i in range(len(data)):
        insertionLabel()
        key = data[i]
        j=i-1
        drawArray(data,['blue' if x == i else 'red' if x==j else 'white' for x in range(len(data))]) 
        root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
        while(j>=0 and key<data[j]):
            data[j+1]=data[j]  
            drawArray(data,['blue' if x == i else 'red' if x==j or x==j+1 else 'white' for x in range(len(data))]) 
            root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
            j =j-1
        data[j+1]=key    
        drawArray(data,['white' for x in range(len(data))])  
        root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
    drawArray(data, ['green' for _ in range(len(data))])

def insertionLabel():
    insertionVar = StringVar()
    insertionVar.set('Insertion Sort Algorithm: \n Insertion sort is a simple sorting algorithm that works by iteratively inserting each element of an unsorted \n list into its correct position in a sorted portion of the list. It is a stable sorting algorithm, meaning that \n elements with equal values maintain their relative order in the sorted output.\n\n Time Complexity: O(n^2)\t\t\tSpace Complexity: O(1)')
    label1 = Label(root,textvariable=insertionVar,font=("Arial", 12, "bold"),justify=LEFT,width=100).grid(row=3)

# Merge sort Algorithm
# Code for joining to sorted arrays
def mergeProcedure(arr,i,mid,j):
    n1 = mid-i+1
    n2 = j-mid

    leftSubarray =[0]*n1
    rightSubarray=[0]*n2

    for m in range(n1):
        leftSubarray[m]=arr[i+m]
    for n in range(n2):
        rightSubarray[n]=arr[mid+1+n]

    p=0
    q=0
    k=i

    while(p<n1 and q<n2):
        drawArray(arr,['blue' if x>=i and x<=j else 'white' for x in range(len(arr))])
        root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
        if leftSubarray[p]<rightSubarray[q]:
            arr[k]=leftSubarray[p]
            p+=1
        else:
            arr[k]=rightSubarray[q]
            q+=1
        k+=1
    while p<n1:
        drawArray(arr,['blue' if x>=i and x<=j else 'white' for x in range(len(arr))])
        root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
        arr[k]=leftSubarray[p]
        p+=1
        k+=1
    while q<n2:
        drawArray(arr,['blue' if x>=i and x<=j else 'white' for x in range(len(arr))])
        root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
        arr[k]=rightSubarray[q]
        q+=1
        k+=1

def  mergeSort(arr,i,j):
    mergeLabel()
    if i == j:
        return arr
    else:
        mid=i+(j-i)//2
        mergeSort(arr,i,mid)
        mergeSort(arr,mid+1,j)
        mergeProcedure(arr,i,mid,j)
    return arr

def mergeLabel():
    mergeVar = StringVar()
    mergeVar.set('Merge Sort Algorithm: \n Merge sort is a divide-and-conquer algorithm used to sort an array or list. It works by splitting the array \n into two halves, sorting each half recursively, and then merging the sorted halves back together. The merging \n process involves comparing the smallest elements of each half and placing the smaller one into the result array.\n This is repeated until all elements are merged in order  \n Time Complexity: O(nlogn)\t\t\tSpace Complexity: O(n)')
    label1 = Label(root,textvariable=mergeVar,font=("Arial", 12, "bold"),justify=LEFT).grid(row=3)


# Calling Merge sort
def callMergeSort():
    i=0
    j=len(data)-1
    mergeSort(data,i,j)
    drawArray(data,['green' for _ in range(len(data))])

# Quick Sort Algorithm
# Partition Algorithm
def  partition(arr,p,q):
    pivot = arr[p]
    i=p
    for j in range(i+1,q+1):
        drawArray(data,['blue' if x == i or x== j else 'white' for x in range(len(data))])
        root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
            drawArray(data,['red' if x == i or x== j else 'white' for x in range(len(data))])
            root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
    arr[i],arr[p]=arr[p],arr[i]
    drawArray(data,['red' if x == i or x== p else 'white' for x in range(len(data))])
    root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
    return i

def quickSort(arr,p,q):
    if p<q:
        m=partition(arr,p,q)
        drawArray(data,['green' if x == m else 'white' for x in range(len(data))])
        root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
        quickSort(arr,p,m-1)
        quickSort(arr,m+1,q)

def quickLabel():
    quickVar = StringVar()
    quickVar.set('Quick Sort Algorithm: \n Quick Sort is an efficient, in-place sorting algorithm that uses a divide-and-conquer approach to sort\n elements. It works by selecting a "pivot" element from the array and partitioning the other elements into two\n sub-arrays according to whether they are less than or greater than the pivot. The pivot is then placed in its\n correct position, and the process is recursively applied to the sub-arrays.\n Time Complexity: O(n^2)(Worst Case)\t\tSpace Complexity: O(1)(Excluding Stack Space)')
    label1 = Label(root,textvariable=quickVar,font=("Arial", 12, "bold"),justify=LEFT,width=100).grid(row=3)

# Calling Quick Sort
def callQuickSort():
    quickLabel()
    p=0
    q=len(data)-1
    quickSort(data,p,q)
    drawArray(data,['green' for _ in range(len(data))])

# Heap Sort Algorithm
def heapify(arr,n,i,size):
    largest=i
    left = 2*i+1
    right = 2*i+2

    if left<n and arr[largest]<arr[left]:
        largest=left
        drawArray(data,['blue' if x == largest else 'green' if x>=size else 'white' for x in range(len(data))])
        root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
    if right<n and arr[largest]<arr[right]:
        largest=right
        drawArray(data,['blue' if x == largest else 'green' if x>=size else 'white' for x in range(len(data))])
        root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
    if largest!=i:
        arr[largest],arr[i]=arr[i],arr[largest]
        drawArray(data,['red' if x == largest or x == i else 'green' if x>=size else 'white' for x in range(len(data))])
        root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
        heapify(arr,n,largest,size)
def heapSort():
    heapLabel()
    n =len(data)
    for i in range(n//2,-1,-1):
        heapify(data,n,i,n+1) # n+1 is just a size variable in this 
    for i in range(n-1,0,-1):
        size = i # it not a variable come from original heap sort it just made to make right colurs
        data[i],data[0]=data[0],data[i]
        drawArray(data,['green' if x>=i else 'white' for x in range(len(data))])
        root.after(int(2000/int(speed_scale.get())))  #Pause to visualize the comparison
        heapify(data,i,0,size)
    drawArray(data,['green' for _ in range(len(data))])

def heapLabel():
    heapVar = StringVar()
    heapVar.set('Heap Sort Algorithm: \n Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort elements.\n It operates in two main phases: building a max heap (or min heap) from the input data and then repeatedly\n extracting the maximum (or minimum) element from the heap and placing it at the end of the sorted section \n of the array.\n Time Complexity: O(nlogn)\t\t\tSpace Complexity: O(1)(Excluding Stack Space)') 
    label1 = Label(root,textvariable=heapVar,font=("Arial", 12, "bold"),justify=LEFT,width=100).grid(row=3)   
    
# Intro Label
def introLabel():
    introVar = StringVar()
    introVar.set('Sorting Algorithms: \n Sorting Algorithms are techniques used to arrange elements of a list or array in a specific order, typically\n in ascending or descending order. They are fundamental in computer science for organizing data, improving\n search efficiency, and enabling various data processing tasks.\n\n')
    label1 = Label(root,textvariable=introVar,font=("Arial", 12, "bold"),justify=LEFT,width = 100).grid(row=3)  
# Function to draw array into bars
def drawArray(data, colorArray):
    canvas.delete("all")
    canvas_height = 480
    canvas_width = 1096
    bar_width = canvas_width / len(data)
    for i, value in enumerate(data):
        x0 = i * bar_width
        y0 = canvas_height - value
        x1 = (i + 1) * bar_width
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
    root.update_idletasks()

#Creating frame at the top
frame = LabelFrame(root,bg='#1B4366' )#ff9f1c
frame.grid(row=0)



# For Sort Button
def select():
    if clicked.get()=='Bubble Sort':
        return bubbleSort()
    elif clicked.get()=='Selection Sort':
        return selectionSort()
    elif clicked.get() == 'Insertion Sort':
        return insertionSort()
    elif clicked.get()  == 'Merge Sort':
        return callMergeSort()
    elif clicked.get() == 'Quick Sort':
        return callQuickSort()
    elif clicked.get() == 'Heap Sort':
        return heapSort()
    

# size box for size controller
sizeBox=LabelFrame(frame,bg='#5ABB72')
sizeBox.grid(row=0,column=5,padx=(45,2))

#Label above the size controller
sizeLabel = Label(sizeBox,text="Array Size",width=15,bg='#5ABB72')
sizeLabel.pack()


#TO control the size of array
sizeController = Scale(sizeBox, from_=5, to=350, orient=HORIZONTAL,bg='#899878')
sizeController.set(35)  # Default speed
sizeController.pack()


def reset():
    global data
    data = [random.randint(10, 450) for _ in range(int(sizeController.get()))]
    drawArray(data, ['white' for _ in range(len(data))])

# Creating Canvas
canvas = Canvas(root, width=1096, height=479, bg='#000000')
canvas.grid(row=1)



#List of Sorting Algorithms
algo = ['Bubble Sort','Selection Sort','Insertion Sort','Merge Sort','Quick Sort','Heap Sort']

clicked = StringVar()
clicked.set(algo[0])

#Algo Box for drop down menu
algoBox=LabelFrame(frame,bg='#5ABB72')
algoBox.grid(row=0,column=0,padx=(2,45))

#Algo Label
algoLabel = Label(algoBox,text='Select Algorithm',bg='#5ABB72')
#algoLabel.grid(row=0,column=0)
algoLabel.pack()

# Drop down algo list
drop = OptionMenu(algoBox, clicked, *algo )
drop.config(bg='#899878')
#drop.grid(row=1,column=0)
drop.pack()


sort = Button(frame, text="Sort",bg='#5ABB72',command=select,width=12) #8BA3B1
resetButton = Button(frame , text="Reset",bg='#5ABB72',command=reset,width=12)
instruction = Button(frame,text='Instructions',bg='#5ABB72',command=instructions,width=12)

sort.grid(row=0,column=2,padx=47)
resetButton.grid(row=0,column=3,padx=47)
instruction.grid(row=0,column=4,padx=47)

# speed box for speed controller
speedBox=LabelFrame(frame,bg='#5ABB72')
speedBox.grid(row=0,column=1,padx=47)

#Label above the speed controller
speedLabel = Label(speedBox,text="Speed controller",width=15,bg='#5ABB72')
speedLabel.pack()

# speed controler
speed_scale = Scale(speedBox, from_=1, to=2000, orient=HORIZONTAL,bg='#899878')
speed_scale.set(500)  # Default speed
speed_scale.pack()

note=Label(root,text='Note: Please select reset after changing array size to implement it and no button will work at time of sorting',font=("Arial", 10, "bold"))
note.grid(row=2)

reset()
introLabel()

root.mainloop()

