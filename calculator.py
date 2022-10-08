from tkinter import *
from tkinter.ttk import *
import re

root = Tk()
root.title("Dragan's App")

style = Style()

style.configure("TButton", font = ("Helvetica", 19, "bold"), foreground = "#fff", background = "#F8F8F8")

def get_buttons(i):
    j = "" if i == 0 else i + 1
    btn = [item for item in root.winfo_children() if item.__getattribute__("_name") == f"!button{j}"][0]
    operation = btn["text"]
    operations = ["X", "-", "+"]
    #if operation is numeric add it to the current_operand
    if operation.isdigit():
        #if operation is 0 and current_operand is empty, it should not do anything
        if operation == "0" and current_operand_text.get() == "":
            pass
        elif first_operand["text"] == "":
            current_operand_text.set(current_operand_text.get() + operation)
        else:
            if ("=" not in first_operand["text"]):
                current_operand_text.set(current_operand_text.get() + operation)
            else:
                current_operand_text.set(operation)
    #if current_operand isn't empty and not isdigit(operation), first_operand will be {f"{current_operand operation}"}
    if current_operand_text.get() != "" and operation in operations:
        first_operand["text"] = f"{current_operand_text.get()} {operation}"
        current_operand_text.set("")
    if operation == "C":
        current_operand_text.set("")
        first_operand["text"] = ""
    if operation == "=":
        if len(first_operand["text"].split(" ")) > 0 and first_operand["text"] != "" and current_operand_text.get() != "":
            s1 = int(first_operand["text"].split(" ")[0])
            operator = first_operand["text"].split(" ")[1]
            s2 = int(current_operand_text.get())
            first_operand["text"] = first_operand["text"] + " " + current_operand_text.get() + " ="
            if operator == "X":
                current_operand_text.set(s1 * s2)
            elif operator == "+":
                current_operand_text.set(s1 + s2)
            else:
                current_operand_text.set(s1 - s2)

first_operand = Label()
first_operand.grid(row = 0, column = 1)

def get_current_operand(text_var):
    if not (text_var.get().isdigit()):
        text_var.set(re.sub("[^0-9]+", "", text_var.get()))

current_operand_text = StringVar()
current_operand_text.trace('w', lambda name, index, mode, text=current_operand_text: get_current_operand(current_operand_text))

current_operand = Entry(root, textvariable=current_operand_text).grid(row = 1, column = 2, columnspan = 2)

BUTTON_VALUES = ["7", "8", "9", "X", "4", "5", "6", "-", "1", "2", "3", "+", "C", "0", ".", "="]

for row in range(2, 6):
    for col in range(4):
        i = row - 2 + col + (row - 2) * 3
        button_text = BUTTON_VALUES[row - 2 + col + (row - 2) * 3]
        #lots of lambda objects within the same namespace that are making reference to names in the outer scope.
        #that means they don't become closures and they don't store references to the objects until later... When it happens, all lambdas will refer to the last value of i.
        #so, variable j is needed here
        Button(root, command = lambda j=i: get_buttons(j), text = button_text).grid(row=row, column=col)

mainloop()