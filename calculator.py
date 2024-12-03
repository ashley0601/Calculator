import tkinter as tk

# Function to handle button click
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Clear the current input
    entry.insert(tk.END, current + value)  # Add the new value to the input

# Function to evaluate the expression
def evaluate():
    try:
        result = eval(entry.get())  # Evaluate the mathematical expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))  # Show the result
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")  # In case of error, show "Error"

# Function to clear the input
def clear():
    entry.delete(0, tk.END)

# Function to remove the last character
def backspace():
    current = entry.get()
    entry.delete(len(current)-1, tk.END)

# Set up the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.config(bg="#ffefff")  # Set background to a light pink color

# Input field
entry = tk.Entry(root, font=("Arial", 20), bg="white", fg="black", bd=10, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Define button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('<', 5, 1)
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Arial", 20), bg="#ff66b2", fg="white", command=evaluate)
    elif text == "C":
        button = tk.Button(root, text=text, font=("Arial", 20), bg="#ff66b2", fg="white", command=clear)
    elif text == "<":
        button = tk.Button(root, text=text, font=("Arial", 20), bg="#ff66b2", fg="white", command=backspace)
    else:
        button = tk.Button(root, text=text, font=("Arial", 20), bg="white", fg="black", command=lambda value=text: button_click(value))
    button.grid(row=row, column=col, sticky="nsew", ipadx=20, ipady=20)

# Make the grid rows and columns expandable
for i in range(6):
    root.grid_rowconfigure(i, weight=1, uniform="equal")
for i in range(4):
    root.grid_columnconfigure(i, weight=1, uniform="equal")

# Run the application
root.mainloop()
