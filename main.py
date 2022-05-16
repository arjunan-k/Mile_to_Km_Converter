from tkinter import *
window = Tk()
window.title("Mile to km Converter")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

input1 = Entry(width=7)
input1.grid(column=1, row=0)

my_label1 = Label(text="Miles", font=("Arial", 16, "bold"))
my_label1.grid(column=2, row=0)

my_label2 = Label(text="is equal to", font=("Arial", 16, "bold"))
my_label2.grid(column=0, row=1)

my_label3 = Label(text="0", font=("Arial", 16, "bold"))
my_label3.grid(column=1, row=1)

my_label4 = Label(text="Km", font=("Arial", 16, "bold"))
my_label4.grid(column=2, row=1)


def miles_to_km():
    b = float(input1.get())
    a = round(b * 1.609, 2)
    my_label3.config(text=f"{a}")


button = Button(text="calculate", command=miles_to_km)
button.grid(column=1, row=2)
window.mainloop()