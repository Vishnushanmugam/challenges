import tkinter as tk

def Flames():
    name1=entry_name1.get()
    name2=entry_name2.get()
    names=name1+name2

    for n in names:
        if names.count(n) !=1:
            names=names.replace(n,"")
            
    number=len(names)%6
    
    f={
        0:"SIBLINGS",
        1:"FRIENDS",
        2:"LOVE",
        3:"AFFECTION",
        4:"MARRIAGE",
        5:"ENEMY",
        
    }
    
    rel=f.get(number)

    result_label.config(text="your relationship is: " +rel)


window=tk.Tk()
window.title("FLAMES GAME")
window.geometry("500x500")

label_header=tk.Label(window,text="JUST FOR FUN GAME",font=("Arial",15),bg="red")
label_header.pack()
label_name1=tk.Label(window,text="Enter your name")
label_name1.pack()
entry_name1=tk.Entry(window,textvariable=tk.StringVar())
entry_name1.pack()
label_name2=tk.Label(window,text="Enter your crush name")
label_name2.pack()
entry_name2=tk.Entry(window,textvariable=tk.StringVar())
entry_name2.pack()

button_result=tk.Button(window,text="SHOW RESULT",bg="yellow",command=Flames).pack()

result_label=tk.Label(window, text="")
result_label.pack()

window.mainloop()