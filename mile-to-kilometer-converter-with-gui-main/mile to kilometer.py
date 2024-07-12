from tkinter import *

window = Tk()
window.title("Miles to Kilometers converter")
window.wm_minsize(300 , 200)
window.config(padx=50 , pady=50)

def button_clicked():
    data = entry.get()
    kilometers = round(int(data) * 1.60934 , 2)
    km.config(text=kilometers)

miles = Label(text="Miles", font=("Arial" , 12))
miles.grid(column=3 , row=1)

button = Button(text="Calculate" , command=button_clicked)
button.grid(column=1, row=3)

entry = Entry()
entry.config(width=15)
entry.insert(END, string="0")
entry.grid(column=1 , row=1)

equal = Label(text="is equal to", font=("Arial" , 12))
equal.grid(column=0 , row=2)

km = Label(text="0", font=("Arial" , 12))
km.grid(column=1 , row=2)

km_lab = Label(text="Km", font=("Arial" , 12))
km_lab.grid(column=3 , row=2)

window.mainloop()