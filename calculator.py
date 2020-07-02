import tkinter as tk
from functools import partial
def mercury(label_result, n1):
    num1 = (n1.get())
    result = int(num1)*0.37
    label_result.config(text="Your weight in kg will be: %d" % result )
    return
def venus(label_result, n1):
    num1 = (n1.get())
    result1 = int(num1)*0.90
    label_result.config(text="Your weight in kg will be: %d" % result1 )
    return

def mars(label_result, n1):
    num1 = (n1.get())
    result2 = int(num1)*0.38
    label_result.config(text="Your weight in kg will be: %d" % result2 )
    return
def jupiter(label_result, n1):
    num1 = (n1.get())
    result3 = int(num1)*2.65
    label_result.config(text="Your weight in kg will be: %d" % result3 )
    return
def saturn(label_result, n1):
    num1 = (n1.get())
    result4 = int(num1)*1.14
    label_result.config(text="Your weight in kg will be: %d" % result4 )
    return
def uranus(label_result, n1):
    num1 = (n1.get())
    result5 = int(num1)*1.07
    label_result.config(text="Your weight in kg will be: %d" % result5 )
    return
def neptune(label_result, n1):
    num1 = (n1.get())
    result6 = int(num1)*1.35
    label_result.config(text="Your weight in kg will be: %d" % result6 )
    return
def pluto(label_result, n1):
    num1 = (n1.get())
    result6 = int(num1)*0.06
    label_result.config(text="Your weight in kg will be: %d" % result6 )
    return
def hd100546(label_result, n1):
    num1 = (n1.get())
    result7 = int(num1)*6.16*10**6
    label_result.config(text="Your weight in kg will be: %d" % result7 )
    return


root = tk.Tk()
root.geometry('500x300+100+200')
root.title('Weight Calculator')
root.iconbitmap('my_logo.ico')
number1 = tk.StringVar()
#number2 = tk.StringVar()
labelTitle = tk.Label(root, text="Weight Calculator").grid(row=0, column=1)
labelNum1 = tk.Label(root, text="Enter your weight on earth").grid(row=2, column=0)
#labelNum2 = tk.Label(root, text="Enter another number").grid(row=2, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=11, column=1)
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=2, column=1)
#entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
mercury = partial(mercury, labelResult, number1)
venus = partial(venus, labelResult, number1)
mars = partial(mars, labelResult, number1)
jupiter = partial(jupiter, labelResult, number1)
saturn = partial(saturn, labelResult, number1)
uranus = partial(uranus, labelResult, number1)
neptune = partial(neptune, labelResult, number1)
pluto = partial(pluto, labelResult, number1)
hd100546 = partial(hd100546, labelResult, number1)

buttonCal = tk.Button(root, text="Mercury", command=mercury,fg="grey").grid(row=6, column=0)
buttonCal = tk.Button(root, text="Venus", command=venus, fg="yellow").grid(row=6, column=1)
buttonCal = tk.Button(root, text="Mars", command=mars, fg="red").grid(row=6, column=2)
buttonCal = tk.Button(root, text="Jupiter", command=jupiter,fg="orange").grid(row=7, column=0)
buttonCal = tk.Button(root, text="Saturn", command=saturn, fg="yellow").grid(row=7, column=1)
buttonCal = tk.Button(root, text="Uranus", command=uranus, fg="green").grid(row=7, column=2)
buttonCal = tk.Button(root, text="Neptune", command=neptune, fg="blue").grid(row=8, column=0)
buttonCal = tk.Button(root, text="Pluto", command=pluto, fg="grey").grid(row=8, column=1)
buttonCal = tk.Button(root, text="HD100546", command=hd100546,fg="red").grid(row=8, column=2)


root.mainloop()
