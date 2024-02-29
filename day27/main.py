from tkinter import *


def button_click():
    print("Calculating temperature ")
    user_string = (int(input.get()) - 32) * (5/9)
    output_label.config(text=user_string)


window = Tk()
window.title("Temperature Converter")
window.minsize(width=300, height=300)
window.config(pady=50, padx=50)

# Label
temp_f = Label(text="temp (F)", font=("Arial", 14, "italic"))
temp_f.grid(column=2, row=0)


equal_label = Label(text="is equal to", font=("Arial", 14, "italic"))
equal_label.grid(column=0, row=1)

output_label = Label(text="0", font=("Arial", 14, "italic"))
output_label.grid(column=1, row=1)

temp_c = Label(text="temp (C)", font=("Arial", 14, "italic"))
temp_c.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)


# Entry
input = Entry(width=10)
input.grid(column=1, row=0)


window.mainloop()


# def add(*args):
#     total_sum = 0
#     for num in args:
#         total_sum += num
#     return total_sum
#
# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     return n


# print(calculate(3, add=2, multiply=4))

