from tkinter import *
from tkinter import messagebox
import lottery

# Create main window
root = Tk()
root.title("Lottery")


# Create Listbox

listbox = Listbox(root, 
                  height=4, 
                  width=30,
                  bg="white",
                  font="Helvetica",
                  fg="blue")

# Defines Size
root.geometry("380x300")

# Create Label
label_amount = Label(root, text="Amount of tickets, max 3:")
label_amount.grid(row=0, column=0, sticky=E, padx=5, pady=5)


# Creates textfield
textbox_amount = Entry(root, width=2)
textbox_amount.grid(row=0, column=1, sticky=W, padx=5, pady=5)
textbox_amount.focus_set()

def update_listbox(amountTickets):
    # Empties the listbox
    listbox.delete(0, END)
    # Adds the prices to the listbox
    listbox.insert(1, "Congratulations! You have won:")

    try:
        int_amountTickets = int(amountTickets)
        i=0 
        if (int_amountTickets < 4):
            while i < int_amountTickets:
                award = lottery.lottery().getAward()
                listbox.insert((i+2), award)
                i+=1




        elif (int_amountTickets > 3):   
            messagebox.showinfo(message="You've chosen too many tickets!") 

    except ValueError:
        messagebox.showinfo(message="Please enter a number")



def ClickRandomButton():
    # print("Press")
    amountTickets = textbox_amount.get()
    # print(f"Tryck! {amountTickets}")

    # Clears the listbox
    listbox.delete(0, END)

    # Changes focus to the first item in the list
    textbox_amount.focus_set()
    update_listbox(amountTickets)





# Creates button
button_random = Button(text="Test your luck!", command=ClickRandomButton)
button_random.grid(row=1, column=0, sticky=E, padx=15, pady=15)

listbox.grid(row=2, column=0, columnspan=2, padx=15, pady=15)


root.mainloop()