import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("this is a first canvas")

label = tk.Label(root, text="this is Label", font=('Arial', 18))
label.pack(padx=20, pady=40)

textbox = tk.Text(root,height=3, font=('Arial', 18))
textbox.pack()

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text='1')
btn1.grid(row=0, column=0, sticky=tk.W+tk.E)

btn2 = tk.Button(buttonframe, text='1')
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text='1')
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text='1')
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text='1')
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text='1')
btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

buttonframe.pack(fill='x')
root.mainloop()

