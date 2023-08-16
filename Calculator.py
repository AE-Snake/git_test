# importing packages

from tkinter import *

# Defining the function for calculation

def btn_click(num):
    global expression
    try:
        ent["state"] = "normal"
        expression += num
        ent.insert(END, num)

        if num == "=":
            res = str(eval(expression[:-1]))
            ent.insert(END, res)
            expression = ""

        ent["state"] = "readonly"
    except ZeroDivisionError:
        ent.delete(0, END)
        ent.insert(0, "Error(division by 0)")
    except SyntaxError:
        ent.delete(0, END)
        ent.insert(0, "Error")

# This function is used to clear the input field

def btn_clear():
    global expression
    expression = ""
    ent["state"] = "normal"
    ent.delete(0, END)
    ent["state"] = "readonly"



if __name__ == '__main__':

    root = Tk()                    # Creating a base window
    root.title("Calculator")
    root.geometry("268x288")       # Setting the window size
    root.resizable(False, False)   # Preventing window changes


    fr = Frame(root)                                                 # Organizes widgets into groups
    fr.grid(row=0, column=0, columnspan=4, sticky="nsew")            # Place the widget in a conditional grid cell
    ent = Entry(fr, width=25, font="Arial 15 bold",state="readonly") # Text input field
    ent.pack(expand=True)                                            # Positioning widgets

# Creating a buttons

    btns = (('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
              )

# Variable expression

    expression = ""

# Сreating a delete button

    btn = Button(root, width=3, height=2, text="C", command=lambda: btn_clear()).grid(row=1, column=3, sticky="nsew")

# Bypassing the buttons in the loop

    for row in range(4):
        for column in range(4):
            Button(root, width=2, height=3, text=btns[row][column],
                   command=lambda row=row, column=column: btn_click(btns[row][column])).grid(row=row+2,
                   column=column, sticky= "nsew", padx=1, pady=1)


    root.mainloop() # To display the window and interact with the user, the window method is called
