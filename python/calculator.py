import tkinter as tk
import tkinter.messagebox as tkm
large_font = ('Verdana',15)

Head=tk.Tk()

Head.title('Calculator')
Head.geometry("370x405")

main=tk.Frame(Head, bg='yellow',pady=20,padx=20)
main.place(x=4,y=9,height=95, width=360)

def onclick(give):
    textbox.insert(tk.END,give)

def clear():
    textbox.delete(0,tk.END)

def equal():
    try:
        get_val=textbox.get()
        ans=int(get_val.replace('²','**2'))
        ans=eval(ans)
        textbox.delete(0,tk.END)
        textbox.insert(0,ans)
    except:
        tkm.showinfo('error', 'invalid input')

def pop():
    cut=textbox.get()
    if cut:
        textbox.delete(len(cut)-1,tk.END)

textbox=tk.Entry(main,textvariable=int,borderwidth='2px', font=large_font)
textbox.place(x=-12,y=-12,height=75,width=270)

AC_button=tk.Button(Head, text='AC',borderwidth='2px',command=clear)
AC_button.place(x=295,y=25, height=60, width=60)


btns_frame=tk.Frame(Head, bg='black', pady=20,padx=20)
btns_frame.place(x=5,y=110 ,height=290, width=360)


one_button=tk.Button(Head, text='1',borderwidth='2px', command=lambda:onclick(1))
one_button.place(x=15,y=120, height=60, width=60)

two_button=tk.Button(Head, text='2',borderwidth='2px',command=lambda:onclick(2))
two_button.place(x=85,y=120, height=60, width=60)

three_button=tk.Button(Head, text='3',borderwidth='2px',command=lambda:onclick(3))
three_button.place(x=155,y=120, height=60, width=60)

four_button=tk.Button(Head, text='4',borderwidth='2px',command=lambda:onclick(4))
four_button.place(x=15,y=190, height=60, width=60)

five_button=tk.Button(Head, text='5',borderwidth='2px',command=lambda:onclick(5))
five_button.place(x=85,y=190, height=60, width=60)

six_button=tk.Button(Head, text='6',borderwidth='2px',command=lambda:onclick(6))
six_button.place(x=155,y=190, height=60, width=60)

seven_button=tk.Button(Head, text='7',borderwidth='2px',command=lambda:onclick(7))
seven_button.place(x=15,y=260, height=60, width=60)

eight_button=tk.Button(Head, text='8',borderwidth='2px',command=lambda:onclick(8))
eight_button.place(x=85,y=260, height=60, width=60)

nine_button=tk.Button(Head, text='9',borderwidth='2px',command=lambda:onclick(9))
nine_button.place(x=155,y=260, height=60, width=60)

zero_button=tk.Button(Head, text='0',borderwidth='2px',command=lambda:onclick(0))
zero_button.place(x=15,y=330, height=60, width=60)

zeros_button=tk.Button(Head, text='.',borderwidth='2px',command=lambda:onclick('.'))
zeros_button.place(x=85,y=330, height=60, width=60)

dot_button=tk.Button(Head, text='x²',borderwidth='2px',command=lambda:onclick('²'))
dot_button.place(x=155,y=330, height=60, width=60)

add_button=tk.Button(Head, text='+',borderwidth='2px',command=lambda:onclick('+'))
add_button.place(x=225,y=330, height=60, width=60)

sub_button=tk.Button(Head, text='-',borderwidth='2px',command=lambda:onclick('-'))
sub_button.place(x=225,y=260, height=60, width=60)

multi_button=tk.Button(Head, text='*',borderwidth='2px',command=lambda:onclick('*'))
multi_button.place(x=225,y=190, height=60, width=60)

div_button=tk.Button(Head, text='/',borderwidth='2px',command=lambda:onclick('/'))
div_button.place(x=225,y=120, height=60, width=60)

modulo_button=tk.Button(Head, text='<-',borderwidth='2px',command=pop)
modulo_button.place(x=295,y=120, height=60, width=60)

plus_minus_button=tk.Button(Head, text='%',borderwidth='2px',command=lambda:onclick('%'))
plus_minus_button.place(x=295,y=190, height=60, width=60)

equal_button=tk.Button(Head, text='=',borderwidth='2px',command=equal)
equal_button.place(x=295,y=260, height=130, width=60)

Head.mainloop()
