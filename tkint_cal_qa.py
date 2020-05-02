from tkinter import *
import math as m

# opening a window with object root
root= Tk()
# giving title name of window is "vivek calculator"
root.title('Vivek calculator')

# defining the entry

e= Entry(root, width=45, borderwidth=8)
e.grid(row=0,column=0,columnspan=4)


# defining button_click functions to type the digits in the entry screen.

def button_click(number):
    old=e.get()
    e.delete(0,END)
    e.insert(0, str(old) + str(number))
    return
# defining clear function to clear the screen

def button_clear():
    e.delete(0,END)

# defining add function

def button_add():
    first_number=e.get()
    global f_num
    global math
    math='add'
    f_num=first_number
    e.delete(0,END)

# defining substraction functions

def button_sub():
    first_number=e.get()
    global f_num
    global math
    math='sub'
    f_num=first_number
    e.delete(0,END)


# defining multiplication functions

def button_multiply():
    first_number=e.get()
    global f_num
    global math
    math='mul'
    f_num=first_number
    e.delete(0,END)

# defining division function
def button_division():
    first_number=e.get()
    global f_num
    global math
    math='div'
    f_num=first_number
    e.delete(0,END)

#defining the powen function

def button_power():
    first_number=e.get()
    global f_num
    global math
    math='power'
    f_num=first_number
    e.delete(0,END)

def button_sqrt():
    first_number=e.get()
    global f_num
    global math
    math='sqrt'
    f_num=first_number
    e.delete(0,END)

# defining equal function

def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math=='add':
        result=float(f_num) + float(second_number)
        e.insert(0,result)
    if math=='sub':
        result = float(f_num) - float(second_number)
        e.insert(0, result)
    if math=='mul':
        result = float(f_num) * float(second_number)
        e.insert(0, result)
    if math=='div':
        result = float(f_num) / float(second_number)
        e.insert(0, result)
    if math=='power':
        result=float(f_num) ** float(second_number)
        e.insert(0,result)
    if math=='sqrt':
        result=m.sqrt(float(f_num))
        e.insert(0,result)


# defining buttons

clicked_1= Button(root, text='1', padx=33,pady=20, bg='#33F4FF', command= lambda: button_click(1) )
clicked_2= Button(root, text='2', padx=33,pady=20, bg='#33F4FF', command= lambda: button_click(2) )
clicked_3= Button(root, text='3', padx=33,pady=20,bg='#33F4FF', command= lambda: button_click(3) )
clicked_4= Button(root, text='4', padx=33,pady=20,bg='#33F4FF', command= lambda: button_click(4) )
clicked_5= Button(root, text='5', padx=33,pady=20,bg='#33F4FF', command= lambda: button_click(5) )
clicked_6= Button(root, text='6', padx=33,pady=20,bg='#33F4FF', command= lambda: button_click(6) )
clicked_7= Button(root, text='7', padx=33,pady=20,bg='#33F4FF', command= lambda: button_click(7) )
clicked_8= Button(root, text='8', padx=33,pady=20,bg='#33F4FF', command= lambda: button_click(8) )
clicked_9= Button(root, text='9', padx=33,pady=20,bg='#33F4FF', command= lambda: button_click(9) )
clicked_0= Button(root, text='0', padx=33,pady=20,bg='#33F4FF', command= lambda: button_click(0) )
clicked_dot= Button(root, text='.', padx=33,pady=20,bg='#33F4FF', command= lambda: button_click('.') )
clicked_percent= Button(root, text='%', padx=33,pady=20,bg='#33F4FF', command= lambda: button_click(0) )
clicked_add= Button(root, text='+', padx=33,pady=20,bg='#33F4FF', command=button_add )
clicked_sub= Button(root, text='-', padx=33,pady=20,bg='#33F4FF', command=button_sub )
clicked_mul= Button(root, text='*', padx=33,pady=20,bg='#33F4FF', command=button_multiply )
clicked_div= Button(root, text='/', padx=33,pady=20,bg='#33F4FF', command=button_division )
clicked_equal= Button(root, text='=', padx=33,pady=20,bg='#33F4FF', command= button_equal )
clicked_power= Button(root, text='p', padx=33,pady=20,bg='#33F4FF', command= button_power )
clicked_sq_root= Button(root, text='√', padx=33,pady=20,bg='#33F4FF', command= button_sqrt )
clicked_clr= Button(root, text='C', padx=33,pady=20,bg='#33F4FF', command= button_clear )


# defining the button place

clicked_7.grid(row=1,column=0)
clicked_8.grid(row=1,column=1)
clicked_9.grid(row=1,column=2)
clicked_mul.grid(row=1,column=3)

clicked_4.grid(row=2,column=0)
clicked_5.grid(row=2,column=1)
clicked_6.grid(row=2,column=2)
clicked_div.grid(row=2,column=3)

clicked_1.grid(row=3,column=0)
clicked_2.grid(row=3,column=1)
clicked_3.grid(row=3,column=2)
clicked_sub.grid(row=3,column=3)

clicked_0.grid(row=4,column=0)
clicked_dot.grid(row=4,column=1)
clicked_percent.grid(row=4,column=2)
clicked_add.grid(row=4,column=3)

clicked_power.grid(row=5,column=0)
clicked_sq_root.grid(row=5,column=1)
clicked_clr.grid(row=5,column=2)
clicked_equal.grid(row=5,column=3)








# initiating the loop for window
root.mainloop()