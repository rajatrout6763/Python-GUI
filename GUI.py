# Program to create a GUI which calculates the equivalent parameters using open and short circuit test
from tkinter import *
from tkinter.font import BOLD


main_window=Tk()
# Assigning the variables
opvolt=DoubleVar()
opcurrent=DoubleVar()
oppower=DoubleVar()
shvolt=DoubleVar()
shcurrent=DoubleVar()
shpower=DoubleVar()
main_window.title("To Find The Equivalent Circuit Parameters")
# Assigning size of the window
main_window.geometry("1920x1080")
# Image to be displayed as icon
main_window.iconbitmap('C:/Users/USER/OneDrive/Desktop/favicon.ico')
# Image to be diplayed as background
bg=PhotoImage(file="C:/Users/USER/OneDrive/Desktop/background.png")
my_label=Label(main_window,image=bg)
my_label.place(x=0,y=0,relheight=1,relwidth=1)
# Creating a new window
def openNewWindow():
    x=DoubleVar()
    a=DoubleVar()
    newWindow=Tk()
    newWindow.title("Results")
    newWindow.geometry("1920x1080")
    Label(newWindow,text="EQUIVALENT CIRCUIT PARAMETERS",font=("Times New Roman",32,BOLD,'underline')).place(x=350,y=50)
    x=(oppower.get())/(opvolt.get()*opcurrent.get())
    crlss=(opvolt.get())/(opcurrent.get()*x)
    a=(1-x**2)**(0.5)
    mginp=(opvolt.get())/(opcurrent.get()*a)
    imp=shvolt.get()/shcurrent.get()
    equires=(shpower.get())/(shcurrent.get()**2)
    equiimp=(imp**2-equires**2)**(0.5)
    Label(newWindow,text="Core Loss Resistance = %sΩ"%str(crlss.__round__(2)),font=("Times New Roman",24,BOLD)).place(x=100,y=150)
    Label(newWindow,text="Magnetising Reactance = %sΩ"%str(mginp.__round__(2)),font=("Times New Roman",24,BOLD)).place(x=100,y=200)
    Label(newWindow,text="Equivalent Resistance = %sΩ"%str(equires.__round__(2)),font=("Times New Roman",24,BOLD)).place(x=100,y=250)
    Label(newWindow,text="Equivalent Leakage Resistance = %sΩ"%str(equiimp.__round__(2)),font=("Times New Roman",24,BOLD)).place(x=100,y=300)


    

# Text to be displayed and input to be taken in the new window
Label(main_window,text="OPEN CIRCUIT TEST",font=("Times New Roman",24,BOLD),bg="white").place(x=350,y=150)
Label(main_window,text="Rated Voltage",font=("Times New Roman",18,),bg="white").place(x=350,y=250)
Label(main_window,text="Rated Current",font=("Times New Roman",18),bg="white").place(x=350,y=350)
Label(main_window,text="Rated Power",font=("Times New Roman",18),bg="white").place(x=350,y=450)
Entry(main_window,textvariable=opvolt,width=20,bg="white").place(x=350,y=300)
Entry(main_window,textvariable=opcurrent,width=20,bg="white").place(x=350,y=400)
Entry(main_window,textvariable=oppower,width=20,bg="white").place(x=350,y=500)
Label(main_window,text="SHORT CIRCUIT TEST",font=("Times New Roman",24,BOLD),bg="white").place(x=850,y=150)
Label(main_window,text="Rated Voltage",font=("Times New Roman",18),bg="white").place(x=850,y=250)
Label(main_window,text="Rated Current",font=("Times New Roman",18),bg="white").place(x=850,y=350)
Label(main_window,text="Rated Power",font=("Times New Roman",18),bg="white").place(x=850,y=450)
Entry(main_window,textvariable=shvolt,width=20,bg="white").place(x=850,y=300)
Entry(main_window,textvariable=shcurrent,width=20,bg="white").place(x=850,y=400)
Entry(main_window,textvariable=shpower,width=20,bg="white").place(x=850,y=500)
Button(main_window,bg="white",text="CALCULATE",font=("Times New Roman",14,BOLD),command=openNewWindow).place(x=1100,y=600)

# Execution
mainloop()

