import tkinter as tk
def Flames():
    a=entry_name1.get()
    b=entry_name2.get()
    for i in a:
        if a.count(i) != 1:
            a = a.replace(" ", "")
            
    for n in b:
        if b.count(n) != 1:
            b = b.replace(" ", "")

    s = a + b
    for f in s:
        if s.count(f) != 1:
            s = s.replace(" ", "")

    w = list(s)

    process = True

    while process:
        rl = w
        cl = rl[0]
        process = "*" in cl
        if process:
            si = cl.index("*")
            a = cl[:si]
            b = cl[si + 1:]
        
    count = len(a) + len(b)

    result = ["FRIEND", "LOVE", "AFFECTION", "MARRIAGE", "ENEMY", "SIBILINGS"]

    while len(result) > 1:
        sid = (count % len(result) - 1)
        if sid >= 0:
            right = result[sid + 1:]
            left = result[: sid]
            result = right + left
        else:
            result = result[: len(result) - 1]
        rel=result[0]

        result_label.config(text="YOUR RELATIONSHIP : " +rel)


window=tk.Tk()
window.title("Flames game")
window.geometry("500x500")

label_header=tk.Label(window,text="FLAMES",font=("Arial",15),bg="red")
label_header.pack()
label_name1=tk.Label(window,text="Enter your name")
label_name1.pack()
entry_name1=tk.Entry(window,textvariable=tk.StringVar())
entry_name1.pack()
label_name2=tk.Label(window,text="Enter your partener name")
label_name2.pack()
entry_name2=tk.Entry(window,textvariable=tk.StringVar())
entry_name2.pack()

button_result=tk.Button(window,text="SHOW RESULT",bg="yellow",command=Flames).pack()

result_label=tk.Label(window, text="")
result_label.pack()

window.mainloop()
