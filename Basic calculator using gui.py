from tkinter import *

root=Tk()
root.title("Calculator")
# input box is created
entry=Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    n=entry.get()
    entry.delete(0, END)
    entry.insert(0, str(n)+str(number))

def button_delete():
    entry.delete(0, END)

def button_sum():
    global f_num
    global math
    math="addition"
    f_num=int(entry.get())
    entry.delete(0,END)

def button_minus():
    global f_num
    global math
    math="subtraction"
    f_num=int(entry.get())
    entry.delete(0,END)

def button_multiply():
    global f_num
    global math
    math="multiplication"
    f_num=int(entry.get())
    entry.delete(0,END)

def button_divide():
    global f_num
    global math
    math="division"
    f_num=int(entry.get())
    entry.delete(0,END)

def button_equalto():
    second_num=entry.get()
    entry.delete(0,END)
    if math=="addition":
        entry.insert(0, f_num+int(second_num))

    elif math=="subtraction":
        entry.insert(0, f_num-int(second_num))

    elif math=="multiplication":
        entry.insert(0, f_num*int(second_num))

    elif math=="division":
        entry.insert(0, f_num/int(second_num))

# buttons are created
button_1=Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2=Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3=Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4=Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5=Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6=Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7=Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8=Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9=Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0=Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_add=Button(root, text="+", padx=40, pady=20, command=button_sum)
button_equal=Button(root, text="=", padx=40, pady=20, command=button_equalto)
button_clear=Button(root, text="clear", padx=40, pady=20, command=button_delete)
button_subtract=Button(root, text="-", padx=40, pady=20, command=button_minus)
button_multiply=Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide=Button(root, text="/", padx=40, pady=20, command=button_divide)

# buttons are arranged in a grid
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_add.grid(row=4, column=3)
button_equal.grid(row=4, column=2)

root.mainloop()
