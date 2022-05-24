#download font to make gui look better from: https://www.dafontfree.io/download/san-francisco-text/
#then go to San-Francisco.zip\San Francisco\SFUIDisplay --> download 'SFUIDisplay-Black.otf'
import tkinter as tk
import sympy as sy
import math
from math import sqrt
from sympy.abc import x
def buttonPress(num):

    global equation_text

    equation_text = equation_text+str(num)
    newtext = equation_text
    h = equation_text.replace("**", "^")
    equation_label.set(h)

def equals():

    global equation_text

    if 'x' in equation_text:
        total = str(sy.solve(equation_text))
        equation_label.set(total+'x')
        equation_text = total
    try:
        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except ZeroDivisionError:
        equation_label.set('Math Error')
        equation_text = ""
    except SyntaxError:
        equation_label.set('Invalid Syntax')
        equation_text = ""


def deletes():
    global equation_text
    length = len(equation_text)
    print(length+1)
    if length>0:
        equation_text = equation_text[:-1]
        tc = equation_text.replace("**", "^")
        equation_label.set(tc)
        if '*' in tc:
            ab = tc.replace('*', '')
            equation_label.set(ab)
        print(equation_text)



def clear():
    global equation_text
    equation_label.set("")
    equation_text = ''

window = tk.Tk()
window.title('Simple Calculator')
HEIGHT = 1
WIDTH = 400
canvas = tk.Canvas(height=HEIGHT, width=WIDTH)
canvas.pack()
equation_text = ''


equation_label = tk.StringVar()


text = tk.Label(window, textvariable=equation_label,font=('SFUIDisplay-Black', 27), bg='white',width=24 ,height=2)
text.pack()

frame = tk.Frame(window)
frame.pack()

button1 = tk.Button(frame, text='1', height=4, width=9, font=('SFUIDisplay-Black',12),
                    command=lambda: buttonPress('1'))
button1.grid(row=0, column=0)

button2 = tk.Button(frame, text='2', height=4, width=9, font=('SFUIDisplay-Black',12),
                    command=lambda: buttonPress('2'))
button2.grid(row=0, column=1)

button3 = tk.Button(frame, text='3', height=4, width=9, font=('SFUIDisplay-Black',12),
                    command=lambda: buttonPress('3'))
button3.grid(row=0, column=2)

button4 = tk.Button(frame, text='4', height=4, width=9, font=('SFUIDisplay-Black',12),
                    command=lambda: buttonPress('4'))
button4.grid(row=1, column=0)

button5 = tk.Button(frame, text='5', height=4, width=9, font=('SFUIDisplay-Black',12),
                    command=lambda: buttonPress('5'))
button5.grid(row=1, column=1)

button6 = tk.Button(frame, text='6', height=4, width=9, font=('SFUIDisplay-Black',12),
                    command=lambda: buttonPress('6'))
button6.grid(row=1, column=2)

button7 = tk.Button(frame, text='7', height=4, width=9, font=('SFUIDisplay-Black',12),
                    command=lambda: buttonPress('7'))
button7.grid(row=2, column=0)

button8 = tk.Button(frame, text='8', height=4, width=9, font=('SFUIDisplay-Black',12),
                    command=lambda: buttonPress('8'))
button8.grid(row=2, column=1)

button9 = tk.Button(frame, text='9', height=4, width=9, font=('SFUIDisplay-Black',12),
                    command=lambda: buttonPress('9'))
button9.grid(row=2, column=2)

button0 = tk.Button(frame, text='0', height=4, width=9, font=('SFUIDisplay-Black',12),
                    command=lambda: buttonPress('0'))
button0.grid(row=3, column=0)

plus = tk.Button(frame, text='+', height=4, width=9, font=('SFUIDisplay-Black',12), bg='gray',
                    command=lambda: buttonPress('+'))
plus.grid(row=0, column=4)

minus = tk.Button(frame, text='-', height=4, width=9, font=('SFUIDisplay-Black',12), bg='gray',
                    command=lambda: buttonPress('-'))
minus.grid(row=1, column=4)

multiply = tk.Button(frame, text='*', height=4, width=9, font=('SFUIDisplay-Black',12), bg='gray',
                    command=lambda: buttonPress('*'))
multiply.grid(row=2, column=4)

devide = tk.Button(frame, text='/', height=4, width=9, font=('SFUIDisplay-Black',12), bg='gray',
                    command=lambda: buttonPress('/'))
devide.grid(row=3, column=4)

equal = tk.Button(frame, text='=', height=4, width=9, font=('SFUIDisplay-Black',12), bg='gray',
                    command=equals)
equal.grid(row=4, column=4)

decimal = tk.Button(frame, text='.', height=4, width=9, font=('SFUIDisplay-Black',12),
                    command=lambda: buttonPress('.'))
decimal.grid(row=3, column=1)

findX = tk.Button(frame, text='x', height=4, width=9, font=('SFUIDisplay-Black',12), bg='gray',
                    command=lambda: buttonPress('x'))
findX.grid(row=3, column=2)

power = tk.Button(frame, text='xʸ', height=4, width=9, font=('SFUIDisplay-Black',12), bg='gray',
                    command=lambda: buttonPress('**('))
power.grid(row=4, column=2)

bracket1 = tk.Button(frame, text='(', height=4, width=9, font=('SFUIDisplay-Black',12), bg='gray',
                    command=lambda: buttonPress('('))
bracket1.grid(row=4, column=0)

bracket2 = tk.Button(frame, text=')', height=4, width=9, font=('SFUIDisplay-Black',12), bg='gray',
                    command=lambda: buttonPress(')'))
bracket2.grid(row=4, column=1)

#sqrt = tk.Button(frame, text='sqrt', height=4, width=9, font=('SFUIDisplay-Black',12), bg='gray',
 #                   command=lambda: sqrt('math.sqrt'))
#sqrt.grid(row=5, column=1)

delete = tk.Button(frame, text='⌫', height=4, width=12, font=('SFUIDisplay-Black',12), bg='#913f3f',
                    command=deletes)
delete.grid(row=0, column=5)

#funcs = tk.Button(frame, text='eq', height=4, width=9, font=('SFUIDisplay-Black',12), bg='gray',
                    #command=func)
#funcs.grid(row=5, column=0)

clear = tk.Button(window, text='CLEAR', height=4, width=12, font=('SFUIDisplay-Black', 15) ,bg="#b0b0b0",
                    command=clear)

clear.pack()


window.mainloop()