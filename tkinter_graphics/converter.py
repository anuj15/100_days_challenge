from tkinter import *


def miles_to_km():
    miles = float(input_mile.get())
    km = miles * 8 / 5
    answer_label.config(text=f"{km}")


window = Tk()
window.title("Mile to KM Converter")
window.config(width=300, height=150, padx=20, pady=20)

input_mile = Entry(width=5)
input_mile.grid(row=0, column=1)

miles_label = Label()
miles_label.config(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label()
equal_label.config(text="is equal to")
equal_label.grid(row=1, column=0)

answer_label = Label()
answer_label.grid(row=1, column=1)

km_label = Label()
km_label.config(text="Km")
km_label.grid(row=1, column=2)

calc_button = Button()
calc_button.config(text="Calculate", command=miles_to_km)
calc_button.grid(row=2, column=1)

window.mainloop()

if __name__ == '__main__':
    print("Start")
