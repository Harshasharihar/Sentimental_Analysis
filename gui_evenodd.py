import tkinter as tk
def check():
    try:
        number = int(num.get())
        if number % 2 == 0:
            lbl.config(text=f"Even number",fg = 'white',bg='green')
        else:
            lbl.config(text=f"Odd number",fg = 'white',bg = 'red')
    except Exception as e:
        lbl.config(text="You enter the floating  digits or other characters..!!")

root  = tk.Tk()
num = tk.Entry(root)
btn = tk.Button(root,text = 'Check',fg = 'white',bg = 'blue',command=check)
num.grid(row = 0,column=0)
btn.grid(row = 0,column=1)
lbl = tk.Label(root,text = "")
lbl.grid(row=1,column=0)
root.mainloop()