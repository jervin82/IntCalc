from tkinter import *
import math

root = Tk()

root.title('Interest Calculator')

bod = Frame(root, bg='#FFFFFF')
bod.pack(side='left')
screen = Frame(root, bg='white')
screen.pack(side='right')

#*** Labels ***
p = Label(bod, text='Principal')
r = Label(bod, text='Interest Rate')
t = Label(bod, text='Borrowing Period')
n = Label(bod, text='Number of Times Compounded')

p.grid(row=0, column=0)
r.grid(row=1, column=0)
t.grid(row=2, column=0)
n.grid(row=3, column=0)

#*** Blanks ***
pblank = Entry(bod)
rblank = Entry(bod)
tblank = Entry(bod)
nblank = Entry(bod)

pblank.insert(0, "0")
rblank.insert(0, "0")
tblank.insert(0, "0")
nblank.insert(0, "0")

pblank.grid(row=0, column=1)
rblank.grid(row=1, column=1)
tblank.grid(row=2, column=1)
nblank.grid(row=3, column=1)


#*** Guts ***
def compintCalc():
    """Calculates compound interest and outputs result"""

    pcalc = int(str(pblank.get()))
    rcalc = float(str(rblank.get()))
    tcalc = int(str(tblank.get()))
    ncalc = float(str(nblank.get()))
    rcalcb = float(rcalc/100)
    step1 = float(1+(rcalcb/ncalc))
    step2 = ncalc*tcalc
    step3 = math.pow(step1, step2)
    step4 = pcalc*step3
    step5 = '$'+str(step4)
    outputtext = Text(screen)
    outputtext.config(bg='grey')
    outputtext.pack(side=BOTTOM)
    outputtext.insert(END, step5)


def simpleintCalc():
    """Calculates simple interest and outputs results"""

    simppcalc = int(str(pblank.get()))
    simprcalc = float(str(rblank.get()))
    simptcalc = int(str(tblank.get()))
    simprcalcb = float(simprcalc/100)
    step1 = simppcalc*simprcalcb*simptcalc
    step2 = '$'+str(step1) + ' accrued'
    outputtext2 = Text(screen)
    outputtext2.config(bg='grey')
    outputtext2.pack(side=BOTTOM)
    outputtext2.insert(END, step2)

def clearbutton():
    """Clears entry fields and inserts zeroes"""

    pblank.delete(0, END)
    rblank.delete(0, END)
    tblank.delete(0, END)
    nblank.delete(0, END)
    pblank.insert(0, "0")
    rblank.insert(0, "0")
    tblank.insert(0, "0")
    nblank.insert(0, "0")

#*** Buttons ***
SimpCalcButton = Button(bod, text='Simple', command=simpleintCalc)
SimpCalcButton.grid(row=1, column=2)

CompCalcButton = Button(bod, text='Compound', command=compintCalc)
CompCalcButton.grid(row=2, column=2)

#ClearButton = Button(bod, text='Clear', command=clearbutton)
#ClearButton.grid(row=3, column=2)


root.geometry('600x115')

root.mainloop()
