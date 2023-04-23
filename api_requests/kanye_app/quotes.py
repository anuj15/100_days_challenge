from tkinter import *

import requests
import urllib3


def show_quote():
    urllib3.disable_warnings()
    response = requests.get(url="https://api.kanye.rest", verify=False)
    response.raise_for_status()
    data = response.json()
    quotation = data["quote"]
    canvas.itemconfig(quote, text=quotation)


window = Tk()
window.title("Kanye Quotes")
window.config(padx=10, pady=10)

canvas = Canvas()
canvas.config(width=500, height=400)
bg_image = PhotoImage(file="background.png")
canvas.create_image(250, 200, image=bg_image)
quote = canvas.create_text(250, 150, text="Quotes goes here...", font=("arial", 16, "italic"), width=250)
canvas.grid(row=0, column=0)

button = Button()
b_image = PhotoImage(file="kanye.png")
button.config(image=b_image, border=0, command=show_quote)
button.grid(row=1, column=0)

window.mainloop()

if __name__ == '__main__':
    print("")
