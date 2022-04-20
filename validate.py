import tkinter  # imports Tkinter module

root = tkinter.Tk()  # creates a root window to place an entry with validation there

def only_numeric_input(P):
    # checks if entry value is an integer or empty and returns an appropriate boolean
    if P.isdigit() or P == "":
        return True
    return False

my_entry = tkinter.Entry(root)  # creates an entry

# shows it in the root window using grid geometry manager
my_entry.grid(row=0, column=0)

# registers a Tcl to Python callback
callback = root.register(only_numeric_input)

my_entry.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation
root.mainloop()  # enters to Tkinter main event loop
